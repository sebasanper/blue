**********************
OpenMDAO Documentation
**********************

OpenMDAO is an open-source high-performance computing platform for systems analysis and multidisciplinary optimization, written in Python.
It enables you to decompose your models, making them easier to build and maintain, while still solving them in a tightly coupled manner with efficient parallel numerical methods.

The OpenMDAO project is primarily focused on supporting gradient based optimization with analytic derivatives to allow you to explore large design spaces with 100's or 1000's of design variables,
but the framework also has a number of parallel computing features that can work with gradient free optimization, mixed integer nonlinear programming, and traditional design space exploration.

User Guide
***************************

These are a collection of tutorial problems that teach you important concepts and techniques for using OpenMDAO.
For new users, you should work through all material in **Getting Started** and **Basic User Guide**.
That represents the minimum set of information you need to understand to be able to work with OpenMDAO models.

You will also find tutorials in the **Advanced User Guide** to be very helpful as you grow more familiar with OpenMDAO,
but you don't need to read these right away.
They explain important secondary concepts that you will run into when working with more complex OpenMDAO models.

.. toctree::
    :maxdepth: 1
    :caption: User Guide
    :name: userguide

    getting_started/index.rst
    basic_guide/index.rst
    advanced_guide/index.rst

Reference Guide:
****************************

These docs are intended to be used by as a reference by more experienced users.
They provide useful code snippets, explain a particular feature in detail,
or document the arguments/options/settings for a specific method, Component, Driver, or Solver.


.. toctree::
    :maxdepth: 1
    :caption: Reference Guide
    :name: referenceguide

    feature_reference/index.rst
    examples/index.rst
    theory_manual/index.rst


Other Useful Docs
*********************

.. toctree::
    :maxdepth: 1
    :caption: Other Docs
    :name: otherdocs

    api_translation/index.rst
    _srcdocs/index.rst
    developer_docs/index.rst