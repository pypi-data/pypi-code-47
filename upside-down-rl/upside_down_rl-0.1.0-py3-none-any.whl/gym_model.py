import typing as ty

import numpy as np
import torch
import torch.utils.data
from grappa import expect
from torch import nn

import upside_down_rl
from upside_down_rl.udrl import TrainItem


class GymModel(upside_down_rl.udrl.ModelInferface):
    def __init__(self, model, state_dim, act_dim):
        self.state_dim = state_dim
        self.act_dim = act_dim
        self.model = model
        self.loss = nn.CrossEntropyLoss()
        self.optim = torch.optim.Adam(self.model.parameters())

    def run(self, observation, delta_t: int, delta_r: int):
        raw = self.model(
            torch.tensor(observation, dtype=torch.float32).unsqueeze(0),
            torch.tensor([delta_t, delta_r], dtype=torch.float32).unsqueeze(0),
        )
        probab = torch.softmax(raw, dim=1).detach().numpy().flatten()
        expect(probab.shape).to.equal((self.act_dim,))
        np.testing.assert_almost_equal(probab.sum(), 1.0, decimal=4)
        return np.random.choice(self.act_dim, p=probab)

    def random_action(self):
        return np.random.choice(self.act_dim)

    def train(self, data: ty.List[TrainItem]):  # pylint: disable=too-many-locals
        state_size = (len(data), self.state_dim)
        state_np_tensors = np.zeros(state_size, dtype=np.float32)
        command_np_tensors = np.zeros((len(data), 2), dtype=np.float32)
        act_np_tensors = np.zeros(len(data), dtype=np.int64)
        for i, dat in enumerate(data):
            state_np_tensors[i] = dat.state
            command_np_tensors[i, :] = [dat.delta_r, dat.delta_t]
            act_np_tensors[i] = dat.action

        state_tensors = torch.tensor(state_np_tensors)
        command_tensors = torch.tensor(command_np_tensors)
        act_tensors = torch.tensor(act_np_tensors)

        data_set = torch.utils.data.TensorDataset(
            state_tensors, command_tensors, act_tensors
        )
        train_len = len(data_set) // 4 * 3
        test_len = len(data_set) - train_len
        train_data, test_data = torch.utils.data.random_split(
            data_set, [train_len, test_len]
        )
        train_data_loader = torch.utils.data.DataLoader(
            train_data, batch_size=32, shuffle=True
        )
        test_data_loader = torch.utils.data.DataLoader(
            test_data, batch_size=32, shuffle=True
        )
        losses, accs, test_losses, test_accs = [], [], [], []
        test_loss_avgs = []
        for i in range(128):
            losses = []
            accs = []
            for st_t, cmd_t, act_t in train_data_loader:
                self.optim.zero_grad()
                preds = self.model(st_t, cmd_t)
                loss_val = self.loss(preds, act_t)
                loss_val.backward()
                torch.nn.utils.clip_grad_norm_(self.model.parameters(), 1)
                self.optim.step()
                losses.append(loss_val.item())
                acc = (preds.argmax(1) == act_t).float().mean()
                accs.append(acc.item())
            test_losses = []
            test_accs = []
            for st_t, cmd_t, act_t in test_data_loader:
                preds = self.model(st_t, cmd_t)
                loss_val = self.loss(preds, act_t).item()
                acc = (preds.argmax(1) == act_t).float().mean().item()
                test_losses.append(loss_val)
                test_accs.append(acc)

            test_loss_avgs.append(np.mean(test_losses))
            if len(test_loss_avgs) > 6 and np.mean(test_loss_avgs[-3:]) >= np.mean(
                test_loss_avgs[-6:-3]
            ):
                print("Halt training at {}".format(i))
                break

        print(
            "Average model loss in last training epoch: ",
            np.mean(losses),
            np.mean(test_losses),
        )
        print(
            "Average model acc in last training epoch: ",
            np.mean(accs),
            np.mean(test_accs),
        )
