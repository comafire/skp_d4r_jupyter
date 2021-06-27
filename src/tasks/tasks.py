from invoke import Collection

import skp_util, skp_env

ns = Collection()

if skp_env.JUPYTER:
    import jupyter
    ns.add_collection(Collection.from_module(jupyter), 'jupyter')

