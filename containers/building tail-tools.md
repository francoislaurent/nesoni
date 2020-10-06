
Install *singularity* from https://sylabs.io/singularity/, download the latest recipe and run::

    sudo singularity build tail-tools-container tail-tools-200901.recipe

This will generate a ``tail-tools-container`` file so that instead of running ``python -m tail-tools <tail-tools-script>``, you can run::

    singularity run tail-tools-container <tail-tools-script>

on any machine with *singularity* installed.

Your local Python distribution may conflict with the packages available in the container.
If you run into Python-related issues, the ``-s`` option can be passed to *python*::

    singularity run tail-tools-container -s <tail-tools-script>

