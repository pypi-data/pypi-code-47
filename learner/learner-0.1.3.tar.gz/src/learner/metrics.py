import torch


def binary_accuracy(y_true, y_pred):
    """Calculate binary accuracy

    Args:
        y_true (torch.Tensor): actual labels
        y_pred (torch.Tensor): predict labels

    Returns:
        float: accuracy value between the predictions and actual values
    """
    with torch.no_grad():
        return torch.mean((y_pred == y_true).float()).item()


def categorical_accuracy(y_true, y_pred):
    """Calculate the categorical accuracy for multi-class problems

    Args:
        y_true (torch.Tensor): actual labels
        y_pred (torch.Tensor): predict labels

    Returns:
        float: accuracy value between the predictions and actual values

    """
    with torch.no_grad():
        _, preds = torch.max(y_pred, 1)
        return torch.mean((preds == y_true).float()).item()
