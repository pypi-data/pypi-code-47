# -*- coding: utf-8 -*-
"""
Created on Thu Nov 28 21:10:40 2019

@author: David
"""
from inspect import getmembers, isfunction
import math


'''Metrics is a compilation of different quality measures derived from a 2x2 
confusion matrix. Each method in the Metrics object takes input in a standard way, 
or can be called via the Metrics.measure() method. Citations for each method are 
in the method docstring, eg help(Metrics.q3)'''

class Metrics():
    '''Simple implementations of quality score metrics. The simple interface is
    to call the helper function 
           Metrics.measure('method', tp=TP, fp=FP, fn=FN, tn=TN) 
         
    where method is the name of the quality measure, and tp, fp, fn, tn are the 
    true positive count, false positive count, false negative count and true 
    negative count respectively. This method will check each value exists. 
    Read the documentation for each method to see if particular 
    values from the confusion matrix are required.
    
    For LaTeX typesetting, include the following at the top of the document:
        
        \newcommand\TP{\mathit{TP}}
        \newcommand\FN{\mathit{FN}}
        \newcommand\TN{\mathit{TN}}
        \newcommand\FP{\mathit{FP}}
        
    '''
    
    def __init__(self, tp=None,fp=None,fn=None, tn=None ):
        '''Create a Metrics object on which all methods can be run. This is not
        necessary'''
        if tp and fp and fn and tn:
            try:
                self.tp = tp
                self.tn = tn
                self.fp = fp
                self.fn = fn
            except:
                raise Exception('All values must be specified')
        else:
            raise Exception('All values must be specified')
            
    def list_metrics( verbose=False):
        '''lists available methods. Use the verbose=True option to get the 
        definitions and method names as a dictionary.'''
        to_exclude = ('list_metrics','measure', 'cite')
        
        functions_list = [o for o in getmembers(Metrics) if isfunction(o[1]) and not o[0] in to_exclude and not o[0].startswith('_')]
        if verbose:
            functions = {}
            for n in functions_list:
                functions[n[0]]=n[1].__doc__
            return functions
        return [x[0] for x in functions_list]
            
    def measure( metric='none', tp=-1, fp=-1,fn=-1,tn=-1):
        '''This calls the particular metric requested, if it exists. A list of 
        metrics can be obtained with the Metrics.list_methods() method'''
        # normalise all data to proportions
        total = fp+tp+fn+tn
        ntp = tp/total
        ntn = tn/total
        nfp = fp/total
        nfn = fn/total
        if hasattr(Metrics, metric):
            return getattr(Metrics,metric,lambda:None)(tp=ntp,fp=nfp,fn=nfn,tn=ntn)

    def measure_all(tp=-1, fp=-1,fn=-1,tn=-1):
        '''returns a dictionary of measure: measurement pairs. Where a measure cannot be calculated
        it is given a value of None.
        
        results = Metrics.measure_all(tp=TP, fp=FP, tn=TN, fn=FN)
        
        '''
        metrics = Metrics.list_metrics()
        results = {}
        for m in metrics:
            try:
                val=Metrics.measure(m, tp=tp,fp=fp, tn=tn,fn=fn)
                results[m] = val
            except:
                results[m] = None
        return results
    
    def cite (metric = 'none'):
        if hasattr(Metrics, metric):
            docstring = getattr(Metrics,metric,lambda:None).__doc__
            citations = [c.split(':',1)[1].strip() for c in docstring.split('\n') if c.strip().startswith('citation:')]
            return citations
            
            
    def _require( *args, nonzero=''):
        '''Internal method to check all values are appropriate.
        Should be called with a list of arguments to test and a list of 
        positions that must be non-zero'''
        try:
            positions = [int(x) for x in nonzero.replace(' ','').split(',')]
        except: 
            raise Exception('non-zero positions should be a comma separated list of 0 based integers in text form')
        if max(positions) >= len(args):
            raise Exception('invalid non-zero value position')
        test = True
        for q in range(len(args)):
            try:
                if q in positions:
                    test = test and (int(args[q]) > 0)
                else:
                    test = test and (int(args[q]) >= 0)
            except:
                raise Exception('Invalid value for test')
        return test
        
    def q1( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q1 = (tp-fp)/(tp+fn)
        
        $\mathit{q1} = \frac{(\TP - \FP )}{(\TP + \FN)}$
        
       
citation: Prothero JW (1966) Biophys J 6, 367-370'''
        Metrics._require(tp, fp,fn, tp+fn, nonzero='3')
        return (tp-fp)/(tp+fn)
    
    def q2 ( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q2 = tp/(tp+fn)
        
        $\mathit{q2} = \frac{\TP}{(\TP + \FN)}$
        
name: true positive rate
name: recall
name: sensitivity
        
citation:  Lewis & Scheraga Arch Biophys Biochem (1971) 144, 576-583
citation:  Nagano J Mol Biol (1973) 75,401-420
citation:  Chou & Fasman Biochemistry (1974) 13, 222-244           '''

        Metrics._require(tp+fn, tp, fn, nonzero='0')
        return tp/(tp+fn)

    def q3( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q3 = (tp+tn)/(tp+tn+fp+fn)
        
        $\mathit{q3} = \frac{\TP + \TN}{\TP + \TN + \FP + \FN}$
 
citation: Kotelchuck & Schegara PNAS (1969) 62,14-21
citation: Lewis et al PNAS (1970) 65, 810-815
citation: Robson & Pain J Mol Biol (1971) 58,237-259
citation: Leberman R J Mol Biol (1971) 55,23-30
citation: Nagano J Mol Biol (1973) 75,401-420
citation: Chou & Fasman Biochemistry (1974) 13, 222-244
        '''
        Metrics._require(tp,fp,tn,fn, tp+fp+tn+fn, nonzero="4")
        return (tp+tn)/(tp+tn+fp+fn)
    
    def q4( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q4 = ((tp/(tp+fn))+(tn/(tn+fp)))/2
        
        $\mathit{q4} = \frac{1}{2}\times ( \frac{\TP }{\TP + \FN} + \frac{\TN }{\TN + \FP} )$
 
citation: Ptitsyn and Finkelstein Biofizika (USSR) (1970) 15, 757-768 (Biophysics 15,785-796)
citation: Chou and Fasman Biochemistry (1974) 13, 222-244
'''
        Metrics._require(tp+fn, fp+tn, tp, tn, fp, fn, nonzero="0,1")
        return ((tp/(tp+fn))+(tn/(tn+fp)))/2

    def q5( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q5 = tp/((tp+fn+fp)/(tn+tp+fp+fn))
        
        $\mathit{q5} = \frac{\TP \times (\TP+\TN+\FP+\FN)}{\TP +\FP + \FN} $
         
citation: Nagano K J Mol Biol (1973) 75,401-420
'''
        Metrics._require(tp,tn,fp,fn, tp+fp+fn, nonzero="4")
        return tp*(tn+tp+fp+fn)/(tp+fn+fp)
        
    def q6( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q6 = (tp + tn)/(fp + fn)
        
        $\mathit{q6} = \frac{\TP + TN}{\FP + \FN}$

citation: Kabat and Wu PNAS (1974) 71, 4217-4220
        '''
        Metrics._require(tp,tn,fp,fn, fp+fn, nonzero="4")
        return (tp + tn)/(fp + fn)
    
    def q7( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        q7 = ((tp * tn)-(fp*fn))/math.sqrt((tn+fn)*(tn+fp)*(tp+fn)*(tp+fp))
        
        $\mathit{q7} =  \frac{((\TP \times \TN) - (\FP \times \FN))}{
        \sqrt{(\TN + \FN) \times (\TN + \FP) \times (\TP + \FN) \times (\TP + \FP)}}$
        
name: Matthews Correlation Coefficient

citation: Matthews BW Biochim Biophys Acta (1975) 405, 442-451
citation: Argos et al. Bioch Biophys Acta (1976) 439, 261-273
citation: Lenstra JA Bioch. Biophys Acta (1977) 491, 333-338
'''
        Metrics._require(tp,fp,tn,fn,tn+fn,tn+fp,tp+fn,tp+fp, nonzero="4,5,6,7")
        return ((tp * tn)-(fp*fn))/math.sqrt((tn+fn)*(tn+fp)*(tp+fn)*(tp+fp))

    def req( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        req = (fp+fn)/(2*tp)
        
        $\mathit{REQ} = \frac{\FP + \FN}{2 \times \TP}$

name: Relative Error Quotient

citation: Martin et al. BMC Bioinformatics (2005) 5, 178
'''
        Metrics._require(tp,fp,fn,nonzero="0")
        return (fp+fn)/(2*tp)
    
    def tanimoto( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        TI = tp/(tp+fp+fn)
        
        $\mathit{TI} = \frac{\TP}{\TP + \FP + \FN}
        
name: Tanimoto Index

citation: Tu K et al Genomics (2004) 84, 922-928
'''
        Metrics._require(tp,fp,fn, tp+fn+fp, nonzero="3")
        return tp/(tp+fp+fn)


    def roc( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        roc = sqrt( (fp/(fp+tn))^2 + (tp/(tp+fn))^2)

        $\mathit{ROC} = sqrt{(\frac{\FP}{\FP+\TN})^2 + (\frac{\TP}{\TP+\FN})^2}
        
name: Receiver Operator Characteristic

citation: derived from Fawcett T HP technical report HPL-2003-4
        '''
        Metrics._require(tp,fp,fn,tn, tp+fn, tn+fp, nonzero="4,5")
        return math.sqrt( (fp/(fp+tn))*(fp/(fp+tn)) + (tp/(tp+fn))*(tp/(tp+fn)))

    def specificity( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        specificity = tn/(fp+tn)
        
citation: Fawcett T HP technical report HPL-2003-4
    '''
        Metrics._require(tn,fp, tn+fp, nonzero="2")
        return tn/(fp+tn)

    def fprate( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        fprate - fp/(fp+tn)
        
        
citation: Fawcett T HP technical report HPL-2003-4
'''
        Metrics._require(tn,fp, tn+fp, nonzero="2")
        return fp/(fp+tn);


    def precision( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
         precision = tp/(tp+fp)

name: Positive Predictive Value
      
citation: Fawcett T HP technical report HPL-2003-4
    '''
        Metrics._require(tp,fp, tp+fp, nonzero="2")
        return tp/(tp+fp)
    
    def accuracy( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        accuracy =(tp+tn)/(tp+fp+tn+fn)
        
citation: Fawcett T HP technical report HPL-2003-4
        '''
        Metrics._require(tp,fp,tn,fn, tp+fp+tn+fn, nonzero="4")
        return (tp+tn)/(tp+fp+tn+fn)
    
    def fscore ( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        fscore= (tp/(tp+fp))*(tp/(tp+fn))
        
citation: Fawcett T HP technical report HPL-2003-4
 
'''
        Metrics._require(tp,fp,tn,fn, tp+fp,tp+fn, nonzero="0")
        return (tp/(tp+fp))*(tp/(tp+fn))

    def f2measure ( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        f2measure= 3 * (tp/(tp+fp))*(tp/(tp+fn)) /(2*(tp/(tp+fp))+(tp/(tp+fn)))
        
note: This weights precision twice as much as recall compared to the f1measure.        

citation: C.J. van Rijsenbergen (1979) Information Retrieval, Butterworths, London.
'''
        Metrics._require(tp,fp,tn,fn, tp+fp,tp+fn, nonzero="0")
        return 3 * (tp/(tp+fp))*(tp/(tp+fn)) /(2*(tp/(tp+fp))+(tp/(tp+fn)))

    def fmeasure ( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        fmeasure= 2 * (tp/(tp+fp))*(tp/(tp+fn)) /((tp/(tp+fp))+(tp/(tp+fn)))

note: This is the evenly weighted harmonic mean of precision and recall
        
citation: C.J. van Rijsenbergen (1979) Information Retrieval, Butterworths, London.
'''
        Metrics._require(tp,fp,tn,fn, tp+fp,tp+fn, nonzero="0")
        return 2 * (tp/(tp+fp))*(tp/(tp+fn)) /((tp/(tp+fp))+(tp/(tp+fn)))
    
    def f0_5measure ( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        f0_5measure= 1.5 * (tp/(tp+fp))*(tp/(tp+fn)) /(0.5*(tp/(tp+fp))+(tp/(tp+fn)))

note: This weights recall twice as much as precision.
        
citation: C.J. van Rijsenbergen (1979) Information Retrieval, Butterworths, London.
'''
        Metrics._require(tp,fp,tn,fn, tp+fp,tp+fn, nonzero="0")
        return 1.5 * (tp/(tp+fp))*(tp/(tp+fn)) /(0.5*(tp/(tp+fp))+(tp/(tp+fn)))
    
    def power( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
         power= tp/fp
'''
        Metrics._require(tp,fp, nonzero="1")
        return tp/fp
     
    def logpower( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        logpower = log10(tp/fp)
         
note: a better scaling for power.
'''
        Metrics._require(tp,fp, nonzero="1")
        return math.log10(tp/fp)

    def bajic_k( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        bajic_k = (tp*tn)/(fp*fn)
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="1,3")
        return (tp*tn)/(fp*fn)

    def chisquare( tp=-1, fp=-1,fn=-1,tn=-1):
        ''' 
        chisquare = (((tp*tn)-(fp*fn))/((tp+fp)*(fn+tn)))^2
         
citation: Pearson 1900 Philosophical Magazine. Series 5. 50 (302): 157–175
'''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        return (((tp*tn)-(fp*fn))/((tp+fp)*(fn+tn)))^2
    
    
    def ctg( tp=-1, fp=-1,fn=-1,tn=-1):
        ''' 
        ctg = sqrt(chisquare/(chisquare+1))
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        cs = (((tp*tn)-(fp*fn))/((tp+fp)*(fn+tn)))^2
        return math.sqrt(cs/(cs+1))

    def yule( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        yule = ((tp*tn)-(fp*fn))/((tp*tn)+(fp*fn))
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        return ((tp*tn)-(fp*fn))/((tp*tn)+(fp*fn))

    def ivesgibbs( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        ivesgibbs = tp + tn - (fp + fn)
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        return tp + tn - (fp + fn)     
    
    def acp( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        acp = ((tn/(tn+fp))+(tp/(tp+fp))+(tp/(tp+fn))+(tn/(tn+fn)))/4
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        return ((tn/(tn+fp))+(tp/(tp+fp))+(tp/(tp+fn))+(tn/(tn+fn)))/4
    
    def acc( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        acc = ((tn/(tn+fp))+(tp/(tp+fp))+(tp/(tp+fn))+(tn/(tn+fn)))/2 -1
        '''
        Metrics._require(tp,fp,tn,fn, nonzero="0,1,2,3")
        return ((tn/(tn+fp))+(tp/(tp+fp))+(tp/(tp+fn))+(tn/(tn+fn)))/2 -1

    def gdip1( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        gdip1 = sqrt(fp*fp +fn*fn)/(tp+tn)
        '''
        Metrics._require(tp,fp,tn,fn,tp+tn, nonzero="4")
        return math.sqrt(fp*fp +fn*fn)/(tp+tn)
    
    def gdip2( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        gdip2 =sqrt(fp*fp +fn*fn)/tp
        '''
        Metrics._require(tp,fp,fn, nonzero="0")
        return math.sqrt(fp*fp +fn*fn)/tp
        
    def gdip3( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        gdip3 =sqrt(fp*fp +fn*fn)/tn
        '''
        Metrics._require(tn,fp,fn, nonzero="0")
        return math.sqrt(fp*fp +fn*fn)/tn

    def hamming( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        hamming = (fp+fn)/(tp+tn+fp+fn)

note: Strictly speaking the Hamming distance is an absolute count. Here it is used as a proportion.
        '''
        Metrics._require(tp,fp,tn,fn, tp+tn+fp+fn, nonzero="4")
        return (fp+fn)/(tp+tn+fp+fn)

    def jaccard( tp=-1, fp=-1,fn=-1,tn=-1):
        '''
        jaccard = tp/(tp+fp+fn)

        '''
        Metrics._require(tp,fp,fn, tp+fp+fn, nonzero="3")
        return  tp/(tp+fp+fn)