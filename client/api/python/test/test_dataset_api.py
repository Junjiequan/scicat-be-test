# coding: utf-8

"""
    dacat-api

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: 2.5.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.dataset_api import DatasetApi


class TestDatasetApi(unittest.TestCase):
    """ DatasetApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.dataset_api.DatasetApi()

    def tearDown(self):
        pass

    def test_dataset_count(self):
        """
        Test case for dataset_count

        Count instances of the model matched by where from the data source.
        """
        pass

    def test_dataset_create(self):
        """
        Test case for dataset_create

        Create a new instance of the model and persist it into the data source.
        """
        pass

    def test_dataset_create_change_stream_get_datasets_change_stream(self):
        """
        Test case for dataset_create_change_stream_get_datasets_change_stream

        Create a change stream.
        """
        pass

    def test_dataset_create_change_stream_post_datasets_change_stream(self):
        """
        Test case for dataset_create_change_stream_post_datasets_change_stream

        Create a change stream.
        """
        pass

    def test_dataset_delete_by_id(self):
        """
        Test case for dataset_delete_by_id

        Delete a model instance by {{id}} from the data source.
        """
        pass

    def test_dataset_exists_get_datasetsid_exists(self):
        """
        Test case for dataset_exists_get_datasetsid_exists

        Check whether a model instance exists in the data source.
        """
        pass

    def test_dataset_exists_head_datasetsid(self):
        """
        Test case for dataset_exists_head_datasetsid

        Check whether a model instance exists in the data source.
        """
        pass

    def test_dataset_find(self):
        """
        Test case for dataset_find

        Find all instances of the model matched by filter from the data source.
        """
        pass

    def test_dataset_find_by_id(self):
        """
        Test case for dataset_find_by_id

        Find a model instance by {{id}} from the data source.
        """
        pass

    def test_dataset_find_one(self):
        """
        Test case for dataset_find_one

        Find first instance of the model matched by filter from the data source.
        """
        pass

    def test_dataset_patch_or_create(self):
        """
        Test case for dataset_patch_or_create

        Patch an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dataset_prototype_count_datablocks(self):
        """
        Test case for dataset_prototype_count_datablocks

        Counts datablocks of Dataset.
        """
        pass

    def test_dataset_prototype_count_origdatablocks(self):
        """
        Test case for dataset_prototype_count_origdatablocks

        Counts origdatablocks of Dataset.
        """
        pass

    def test_dataset_prototype_create_datablocks(self):
        """
        Test case for dataset_prototype_create_datablocks

        Creates a new instance in datablocks of this model.
        """
        pass

    def test_dataset_prototype_create_datasetlifecycle(self):
        """
        Test case for dataset_prototype_create_datasetlifecycle

        Creates a new instance in datasetlifecycle of this model.
        """
        pass

    def test_dataset_prototype_create_origdatablocks(self):
        """
        Test case for dataset_prototype_create_origdatablocks

        Creates a new instance in origdatablocks of this model.
        """
        pass

    def test_dataset_prototype_delete_datablocks(self):
        """
        Test case for dataset_prototype_delete_datablocks

        Deletes all datablocks of this model.
        """
        pass

    def test_dataset_prototype_delete_origdatablocks(self):
        """
        Test case for dataset_prototype_delete_origdatablocks

        Deletes all origdatablocks of this model.
        """
        pass

    def test_dataset_prototype_destroy_by_id_datablocks(self):
        """
        Test case for dataset_prototype_destroy_by_id_datablocks

        Delete a related item by id for datablocks.
        """
        pass

    def test_dataset_prototype_destroy_by_id_origdatablocks(self):
        """
        Test case for dataset_prototype_destroy_by_id_origdatablocks

        Delete a related item by id for origdatablocks.
        """
        pass

    def test_dataset_prototype_destroy_datasetlifecycle(self):
        """
        Test case for dataset_prototype_destroy_datasetlifecycle

        Deletes datasetlifecycle of this model.
        """
        pass

    def test_dataset_prototype_find_by_id_datablocks(self):
        """
        Test case for dataset_prototype_find_by_id_datablocks

        Find a related item by id for datablocks.
        """
        pass

    def test_dataset_prototype_find_by_id_origdatablocks(self):
        """
        Test case for dataset_prototype_find_by_id_origdatablocks

        Find a related item by id for origdatablocks.
        """
        pass

    def test_dataset_prototype_get_datablocks(self):
        """
        Test case for dataset_prototype_get_datablocks

        Queries datablocks of Dataset.
        """
        pass

    def test_dataset_prototype_get_datasetlifecycle(self):
        """
        Test case for dataset_prototype_get_datasetlifecycle

        Fetches hasOne relation datasetlifecycle.
        """
        pass

    def test_dataset_prototype_get_origdatablocks(self):
        """
        Test case for dataset_prototype_get_origdatablocks

        Queries origdatablocks of Dataset.
        """
        pass

    def test_dataset_prototype_patch_attributes(self):
        """
        Test case for dataset_prototype_patch_attributes

        Patch attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dataset_prototype_update_by_id_datablocks(self):
        """
        Test case for dataset_prototype_update_by_id_datablocks

        Update a related item by id for datablocks.
        """
        pass

    def test_dataset_prototype_update_by_id_origdatablocks(self):
        """
        Test case for dataset_prototype_update_by_id_origdatablocks

        Update a related item by id for origdatablocks.
        """
        pass

    def test_dataset_prototype_update_datasetlifecycle(self):
        """
        Test case for dataset_prototype_update_datasetlifecycle

        Update datasetlifecycle of this model.
        """
        pass

    def test_dataset_replace_by_id_post_datasetsid_replace(self):
        """
        Test case for dataset_replace_by_id_post_datasetsid_replace

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dataset_replace_by_id_put_datasetsid(self):
        """
        Test case for dataset_replace_by_id_put_datasetsid

        Replace attributes for a model instance and persist it into the data source.
        """
        pass

    def test_dataset_replace_or_create_post_datasets_replace_or_create(self):
        """
        Test case for dataset_replace_or_create_post_datasets_replace_or_create

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dataset_replace_or_create_put_datasets(self):
        """
        Test case for dataset_replace_or_create_put_datasets

        Replace an existing model instance or insert a new one into the data source.
        """
        pass

    def test_dataset_update_all(self):
        """
        Test case for dataset_update_all

        Update instances of the model matched by {{where}} from the data source.
        """
        pass

    def test_dataset_upsert_with_where(self):
        """
        Test case for dataset_upsert_with_where

        Update an existing model instance or insert a new one into the data source based on the where criteria.
        """
        pass


if __name__ == '__main__':
    unittest.main()
