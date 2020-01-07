from ase import Atoms
from .core import BaseParticle
from .core.geometry import get_symmetries, get_standardized_structure
from .core.form import setup_forms


class SingleCrystal(BaseParticle):
    """
    A `SingleCrystal` object is a Wulff construction of a single
    crystalline particle, i.e., a standard Wulff construction.

    Parameters
    ----------
    surface_energies
        A dictionary with surface energies, where keys are
        Miller indices and values surface energies (per area)
        in a unit of choice, such as J/m^2.
    primitive_structure
        primitive cell to implicitly define the point group as
        well as the atomic structure used if an atomic structure
        is requested. By default, an Au FCC structure is used.
    natoms
        Together with `primitive_structure`, this parameter
        defines the volume of the particle. If an atomic structure
        is requested, the number of atoms will as closely as possible
        match this value.
    tol
        Numerical tolerance parameter.

    Example
    -------
    The following example illustrates some possible uses of a
    `SingleCrystal` object::

        >>> from wulffpack import SingleCrystal
        >>> from ase.build import bulk
        >>> from ase.io import write
        >>> surface_energies = {(1, 1, 0): 1.0, (1, 0, 0): 1.08}
        >>> prim = bulk('W', a=3.16, crystalstructure='bcc')
        >>> particle = SingleCrystal(surface_energies, prim)
        >>> particle.view()
        >>> write('single_crystal.xyz', particle.atoms) # Writes atomic structure to file

    """

    def __init__(self, surface_energies: dict,
                 primitive_structure: Atoms = None,
                 natoms: int = 1000,
                 tol: float = 1e-5):
        standardized_structure = get_standardized_structure(primitive_structure)
        symmetries = get_symmetries(standardized_structure)
        forms = setup_forms(surface_energies,
                            standardized_structure.cell.T,
                            symmetries,
                            symmetries)
        super().__init__(forms=forms,
                         standardized_structure=standardized_structure,
                         natoms=natoms,
                         tol=tol)

    @property
    def atoms(self):
        """
        Returns an ASE Atoms object
        """
        return self._get_atoms()
