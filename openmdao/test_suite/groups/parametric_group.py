"""Define the test group classes."""
from __future__ import division, print_function

from openmdao.core.group import Group


class ParametericTestGroup(Group):
    """
    Test Group expected by `ParametricInstance`. Groups inheriting from this should extend
    `default_params` to include valid parametric options for that model.

    Attributes
    ----------
    expected_totals : dict or None
        Dictionary mapping (out, in) pairs to the associated total derivative. Optional
    total_of : iterable
        Iterable containing which outputs to take the derivative of.
    total_wrt : iterable
        Iterable containing which variables with which to take the derivative of the above.
    expected_values : dict or None
        Dictionary mapping variable names to expected values. Optional.
    default_params : dict
        Dictionary containing the available options and default values for parametric sweeps.
    """
    def __init__(self, **kwargs):

        self.expected_totals = None
        self.total_of = None
        self.total_wrt = None
        self.expected_values = None
        self.default_params = {
            'vector_class': ['default', 'petsc'],
            'assembled_jac': [True, False],
            'jacobian_type': ['matvec', 'dense', 'sparse-coo', 'sparse-csr',
                              'sparse-csc'],
        }

        super(ParametericTestGroup, self).__init__()

        self.metadata.declare('vector_class', default='default',
                              values=['default', 'petsc'],
                              type_=str,
                              desc='Which vector implementation to use.')
        self.metadata.declare('assembled_jac', default=True,
                              type_=bool,
                              desc='If an assemebled Jacobian should be used.')
        self.metadata.declare('jacobian_type', default='matvec',
                              type_=str,
                              values=['dense', 'matvec', 'sparse-coo', 'sparse-csr', 'sparse-csc'],
                              desc='Controls the type of the assembled jacobian.')

        self.metadata.update(kwargs)
