import torch
import torch.nn as nn


class Decoder(nn.Module):
    """
    Base class for implementing decoders.
    """

    def __init__(self, num_in, num_out, in_dim):
        """
        Parameters
        ----------
            num_in: int
                Number of input units for a forward pass of the coder. (number of device: N)
            num_out: int
                Number of output units from a forward pass of the coder. (number of split data: K)
            in_dim: tuple
                Dimension of the input data for a forward pass of the coder. shape: (channel, height, width)
        """
        super().__init__()
        self.num_in = num_in
        self.num_out = num_out
        self.in_dim = in_dim
        self.out_dim = in_dim

    def forward(self, datasets: list[torch.Tensor]) -> list[torch.Tensor]:
        """
        Parameters
        ----------
            datasets: list of ``torch.autograd.Variable``
                Input data for a forward pass of the decoder.
        """
        pass
