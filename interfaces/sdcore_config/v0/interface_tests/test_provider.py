# Copyright 2024 Canonical
# See LICENSE file for licensing details.

from interface_tester import Tester
from scenario import State, Relation
import json


def test_no_data_on_created():
    t = Tester()
    state_out = t.run("sdcore-config-relation-created")
    t.assert_relation_data_empty()


def test_data_published_on_created():
    t = Tester(
        State(
            relations=[
                Relation(
                    endpoint="sdcore_config",
                    interface="sdcore_config",
                )
            ],
        )
    )
    state_out: State = t.run("sdcore-config-relation-created")
    t.assert_relation_data_empty()


def test_data_published_on_joined():
    t = Tester(
        State(
            relations=[
                Relation(
                    endpoint="sdcore_config",
                    interface="sdcore_config",
                )
            ],
        )
    )
    state_out: State = t.run("sdcore-config-relation-joined")
    t.assert_schema_valid()


def test_no_data_on_broken():
    valid_app_data = {
        "webui_url": "sdcore-webui-k8s:9876",
    }
    relation = Relation(
        endpoint="sdcore_config",
        interface="sdcore_config",
        local_app_data=valid_app_data,
    )

    t = Tester(State(relations=[relation]))
    state_out: State = t.run("sdcore-config-relation-broken")
    t.assert_relation_data_empty()
