import pytest


def always_returns_true():
    return a(12345)


def test_always_returns_true():
    assert always_returns_true()
