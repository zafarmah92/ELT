from ownerjobs import defs


def test_defs_can_load():
    assert defs.get_implicit_global_asset_job_def()
    assert defs.get_job_def("all_assets")
