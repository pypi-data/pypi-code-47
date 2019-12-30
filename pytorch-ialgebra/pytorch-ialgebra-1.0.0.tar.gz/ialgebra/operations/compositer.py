from ialgebra.utils.utils_interpreter import *
from ialgebra.utils.utils_data import to_numpy, to_tensor

name2identity = {
    'grad_cam': 'GradCam',
    'grad_saliency': 'GradSaliency',
    'guided_backprop_grad': 'GuidedBackpropGrad',
    'guided_backprop_smoothgrad': 'GuidedBackpropSmoothGrad',
    'mask': 'Mask',
    'smoothgrad': 'SmoothGrad'
}

class Compositer(object):
    """
    *Function*: 
    composite saliency_maps to meet user demands
    operators: ['slct',   'proj',  'join', 'anjo']
    queries:   ['select', 'where', 'join', 'left join']

    *Inputs*:
    :input:
    :model:
    :int_map: saliency_map generated by identity
    :interpreter_params:  set default if no user inputs
    :operator_params:

    *Returns*:
    :opt_map: shape = [B*C*H*W], type = numpy.ndarray
    :opt_map+img (might not use): shape = [B*C*H*W], type = numpy.ndarray 
    """

    def __init__(self, identity_name=None, dataset=None,  target_layer=None, device=None):
        # parsing identity
        self.identity = identity_name
        self.dataset = dataset
        self.target_layer = target_layer
        self._identity_class = getattr(getattr(__import__("ialgebra"), "interpreters"), name2identity[self.identity])
        # self.identity_interpreter = self._identity_class(self.model, self.dataset)



    ###### TWO Pairs ######
    # select * from f(x) where w
    def slct_proj(self,  bx, by, model, region):
        """
        *Function*
        :combinition of 'selection' and 'projection':

        *Inputs*:
        :1 input: x
        :1 model: f
        :region: [pos0, pos1, pos2, pos3]

        *Returns*:
        :opt_map: shape = [B*C*H*W], type = numpy.ndarray
        :opt_map+img: shape = [B*C*H*W], type = numpy.ndarray 
        """
        identity_interpreter = self._identity_class(model, self.dataset)
        pos0, pos1, pos2, pos3 = region[0], region[1], region[2], region[3]
        img = bx
        mat = torch.zeros(img.shape)
        roi = img[:, int(pos0):int(pos1), int(pos2):int(pos3)]
        mat[:, int(pos0):int(pos1), int(pos2):int(pos3)] = roi
        mat = mat.to(device)

        heatmap, heatmapimg = identity_interpreter(mat, by)
        return heatmap, heatmapimg 
    


    # select * from f(x) join (select * from f(x'))
    def slct_join(self,  bx_list, by_list,  model, region1, region2):
        """
        *Function*
        :combinition of 'selection' and 'join':

        *Inputs*:
        :2 input: x, x'
        :1 model: f

        *Returns*:
        :common heatmap: 
        :heatmapimg1:  
        :heatmapimg2: 
        """

        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        # bx.size=(1,3,W,H); by.size=(1)
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        identity_interpreter = self._identity_class(model, self.dataset)

        pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
        mat1 = torch.zeros(bx1.shape)
        roi1 = bx1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
        mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1

        mat1 = mat1.to(device)

        pos2_0, pos2_1, pos2_2, pos2_3 = region2[0], region2[1], region2[2], region2[3]
        mat2 = torch.zeros(bx2.shape)
        roi2 = bx1[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)]
        mat2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)] = roi2
        mat2 = mat2.to(device)

        heatmap1, heatmapimg1 = identity_interpreter(mat1, by1)
        heatmap2, heatmapimg2 = identity_interpreter(mat2, by2)

        heatmap = 0.5 * (heatmap1 + heatmap2)
        heatmapimg1 =  heatmap + np.float32(to_numpy(mat1))
        heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)
        heatmapimg2 =  heatmap + np.float32(to_numpy(mat2))
        heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap, heatmapimg1, heatmapimg2


    # select * from f(x) left join (select * from f(x'))
    def slct_anjo(self, bx_list, by_list, model_list, region1, region2 = None, model_diff= False):
        """
        *Function*
        :combinition of 'selection' and 'anti-join':

        *Inputs*:
        case1:  2 input: x, x';   1 model: f
        case2:  1 input: x;       2 models: f, f'

        *Returns*:
        :heatmap1
        :heatmapimg1
        :heatmap2
        :heatmapimg2
        """

        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        model1, model2 = model_list[0], model_list[1]
        identity_interpreter1 = self._identity_class(model1, self.dataset)
        identity_interpreter2 = self._identity_class(model2, self.dataset)


        if model_diff:
            bx, by = bx1, by1
            pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
            mat1 = torch.zeros(bx.shape)
            roi1 = bx[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
            mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1
            mat1 = mat1.to(device)

            heatmap1_1, heatmapimg1_1 = identity_interpreter1(mat1, by1)  # interpreter1_cls1
            heatmap1_2, heatmapimg1_2 = identity_interpreter2(mat1, by1)  # interpreter2_cls1
            heatmap2_1, heatmapimg2_1 = identity_interpreter1(mat1, by2)  # interpreter1_cls2
            heatmap2_2, heatmapimg2_2 = identity_interpreter2(mat1, by2)  # interpreter2_cls2

            heatmap1 = 0.5 * (heatmap1_1 + heatmap2_1)
            heatmapimg1 =  heatmap1 + np.float32(to_numpy(bx))
            heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)

            heatmap2 = 0.5 * (heatmap1_2 + heatmap2_2)
            heatmapimg2 =  heatmap2 + np.float32(to_numpy(bx))
            heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)


        else:
            pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
            mat1 = torch.zeros(bx1.shape)
            roi1 = bx1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
            mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1
            mat1 = mat1.to(device)

            pos2_0, pos2_1, pos2_2, pos2_3 = region2[0], region2[1], region2[2], region2[3]
            mat2 = torch.zeros(bx2.shape)
            roi2 = bx2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)]
            mat2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)] = roi2
            mat2 = mat2.to(device)

            heatmap1_1, heatmapimg1_1 = identity_interpreter1(mat1, by1)  # interpreter1_cls1_input1
            heatmap1_2, heatmapimg1_2 = identity_interpreter2(mat1, by2)  # interpreter2_cls2_input1
            heatmap2_1, heatmapimg2_1 = identity_interpreter1(mat2, by1)  # interpreter1_cls1_input2
            heatmap2_2, heatmapimg2_2 = identity_interpreter2(mat2, by2)  # interpreter2_cls2_input2

            heatmap1 = 0.5 * (heatmap1_1 + heatmap2_1)
            heatmapimg1 =  heatmap1 + np.float32(to_numpy(bx1))
            heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)

            heatmap2 = 0.5 * (heatmap1_2 + heatmap2_2)
            heatmapimg2 =  heatmap2 + np.float32(to_numpy(bx2))
            heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap1, heatmapimg1, heatmap2, heatmapimg2 





    # select * from f(x1)  join  (select * from f(x2) join (select * from f(x3)))
    def proj_join(self,bx_list, by_list, model):
        """
        *Function*
        :combinition of 'projection' and 'join':

        *Inputs*:
        :2 input: x, x'
        :1 model: f

        *Returns*:
        :common heatmap: 
        :heatmapimg1:  
        :heatmapimg2: 
        """
        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        identity_interpreter = self._identity_class(model, self.dataset)

        heatmap1, heatmapimg1 = identity_interpreter(bx1, by1)
        heatmap2, heatmapimg2 = identity_interpreter(bx2, by2)
        heatmap = 0.5 * (heatmap1 + heatmap2)
        heatmapimg1 =  heatmap + np.float32(to_numpy(bx1))
        heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)
        heatmapimg2 =  heatmap + np.float32(to_numpy(bx2))
        heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap, heatmapimg1, heatmapimg2



    def proj_anjo(self, bx_list, by_list, model_list, model_diff= False):
        """
        *Function*: 
        :combinition of 'projection' and 'anti-join', similar to operator 'anti-join' but layer is controled by 'projection'

        *Inputs*:
        :2 inputs: x, x'
        :1 model: f

        *Returns*:
        :heatmap1
        :heatmapimg1
        :heatmap2
        :heatmapimg2
        """

        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        # bx.size=(1,3,W,H); by.size=(1)
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        model1, model2 = model_list[0], model_list[1]
        identity_interpreter1 = self._identity_class(model1, self.dataset)
        identity_interpreter2 = self._identity_class(model2, self.dataset)

        # case1: 1 input, 2 models
        if model_diff:
            heatmap1_1, heatmapimg1_1 = self.identity_interpreter1(bx1, by1)  # interpreter1_cls1
            heatmap1_2, heatmapimg1_2 = self.identity_interpreter2(bx1, by1)  # interpreter2_cls1
            heatmap2_1, heatmapimg2_1 = self.identity_interpreter1(bx1, by2)  # interpreter1_cls2
            heatmap2_2, heatmapimg2_2 = self.identity_interpreter2(bx1, by2)  # interpreter2_cls2

        # case2: 2 inputs, 1 model
        else:
            heatmap1_1, heatmapimg1_1 = identity_interpreter1(bx1, by1)  # interpreter1_cls1_input1
            heatmap1_2, heatmapimg1_2 = identity_interpreter2(bx1, by2)  # interpreter2_cls2_input1
            heatmap2_1, heatmapimg2_1 = identity_interpreter1(bx2, by1)  # interpreter1_cls1_input2
            heatmap2_2, heatmapimg2_2 = identity_interpreter2(bx2, by2)  # interpreter2_cls2_input2

        heatmap1 = 0.5 * (heatmap1_1 + heatmap2_1)
        heatmapimg1 =  heatmap1 + np.float32(to_numpy(bx1))
        heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)

        heatmap2 = 0.5 * (heatmap1_2 + heatmap2_2)
        heatmapimg2 =  heatmap2 + np.float32(to_numpy(bx2))
        heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap1, heatmapimg1, heatmap2, heatmapimg2 


    ###### THREE Pairs ######
    def slct_proj_join(self, bx_list, by_list, model, region1, region2):
        """
        *Function*
        :combinition of 'selection', 'projection' and 'join', similar to compositer 'slct_join'

        *Inputs*:
        :2 input: x, x'
        :1 model: f

        *Returns*:
        :common heatmap: 
        :heatmapimg1:  
        :heatmapimg2: 
        """
        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        identity_interpreter = self._identity_class(model, self.dataset)

        pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
        mat1 = torch.zeros(bx1.shape)
        roi1 = bx1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
        mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1
        mat1 = mat1.to(device)

        pos2_0, pos2_1, pos2_2, pos2_3 = region2[0], region2[1], region2[2], region2[3]
        mat2 = torch.zeros(bx2.shape)
        roi2 = bx1[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)]
        mat2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)] = roi2
        mat2 = mat2.to(device)

        heatmap1, heatmapimg1 = identity_interpreter(mat1, by1)
        heatmap2, heatmapimg2 = identity_interpreter(mat2, by2)

        heatmap = 0.5 * (heatmap1 + heatmap2)
        heatmapimg1 =  heatmap + np.float32(to_numpy(mat1))
        heatmapimg1 = (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)
        heatmapimg2 =  heatmap + np.float32(to_numpy(mat2))
        heatmapimg2 = (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap, heatmapimg1, heatmapimg2


    def slct_proj_anjo(self, bx_list, by_list, model_list, region1, region2 = None, model_diff= False):
        """
        *Function*
        :combinition of 'selection', 'projection' and 'anti-join', similar to compositer 'slct_anjo'

        *Inputs*:
        case1:  2 input: x, x';   1 model: f
        case2:  1 input: x;       2 models: f, f'

        *Returns*:
        :heatmap1
        :heatmapimg1
        :heatmap2
        :heatmapimg2
        """

        bx1, by1, bx2, by2 = bx_list[0], by_list[0], bx_list[1], by_list[1]
        [bx1, bx2] = [b.unsqueeze(0) if len(b.size()) == 3 else b for b in (bx1, bx2)]
        [by1, by2] = [b.unsqueeze(0) if len(b.size()) == 0 else b for b in (by1, by2)]
        model1, model2 = model_list[0], model_list[1]
        identity_interpreter1 = self._identity_class(model1, self.dataset)
        identity_interpreter2 = self._identity_class(model2, self.dataset)

        if model_diff:
            pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
            mat1 = torch.zeros(bx1.shape)
            roi1 = bx1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
            mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1
            mat1 = mat1.to(device)

            heatmap1_1, heatmapimg1_1 = identity_interpreter1(mat1, by1)  # interpreter1_cls1
            heatmap1_2, heatmapimg1_2 = identity_interpreter2(mat1, by1)  # interpreter2_cls1
            heatmap2_1, heatmapimg2_1 = identity_interpreter1(mat1, by2)  # interpreter1_cls2
            heatmap2_2, heatmapimg2_2 = identity_interpreter2(mat1, by2)  # interpreter2_cls2

        else:
            pos1_0, pos1_1, pos1_2, pos1_3 = region1[0], region1[1], region1[2], region1[3]
            mat1 = torch.zeros(bx1.shape)
            roi1 = bx1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)]
            mat1[:, int(pos1_0):int(pos1_1), int(pos1_2):int(pos1_3)] = roi1
            mat1 = mat1.to(device)

            pos2_0, pos2_1, pos2_2, pos2_3 = region2[0], region2[1], region2[2], region2[3]
            mat2 = torch.zeros(bx2.shape)
            roi2 = bx2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)]
            mat2[:, int(pos2_0):int(pos2_1), int(pos2_2):int(pos2_3)] = roi2
            mat2 = mat2.to(device)

            heatmap1_1, heatmapimg1_1 = identity_interpreter1(mat1, by1)  # interpreter1_cls1_input1
            heatmap1_2, heatmapimg1_2 = identity_interpreter2(mat1, by2)  # interpreter2_cls2_input1
            heatmap2_1, heatmapimg2_1 = identity_interpreter1(mat2, by1)  # interpreter1_cls1_input2
            heatmap2_2, heatmapimg2_2 = identity_interpreter2(mat2, by2)  # interpreter2_cls2_input2

        heatmap1 = 0.5 * (heatmap1_1 + heatmap2_1)
        heatmapimg1 =  heatmap1 + np.float32(to_numpy(bx1))
        heatmapimg1 =  (heatmapimg1 / np.max(heatmapimg1)).squeeze(0)

        heatmap2 = 0.5 * (heatmap1_2 + heatmap2_2)
        heatmapimg2 =  heatmap2 + np.float32(to_numpy(bx2))
        heatmapimg2 =  (heatmapimg2 / np.max(heatmapimg2)).squeeze(0)

        return heatmap1, heatmapimg1, heatmap2, heatmapimg2 



