from catalyst.data.dataset import _Path, PathsDataset


def test_PathsDataset() -> None:
    def get_target(path: _Path) -> int:
        result = str(path).split(".")[0].split("_")[1]
        result = int(result)

        return result

    def identity(x):
        return x

    filenames = ["path1_1.jpg", "path2_1.jpg", "path_0.jpg"]
    targets = [1, 1, 0]

    dataset = PathsDataset(filenames, open_fn=identity, label_fn=get_target)

    result = True
    for data, target in zip(dataset.data, targets):
        result &= data["targets"] == target
        assert result
