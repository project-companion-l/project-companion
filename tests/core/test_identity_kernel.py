from companion.core.identity_kernel import IdentityKernel


def test_identity_name():
    identity = IdentityKernel()

    assert identity.name == "Project Companion"


def test_identity_values():
    identity = IdentityKernel()

    assert "誠実" in identity.values