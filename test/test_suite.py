"""Run all tests."""
import os
import unittest
import warnings

import test_data_setup as ds
import test_data_clean as dc
import test_ads_fp_gen as afp
import test_bulk_fp_gen as bfp
import test_feature_optimization as ft
import test_hierarchy_cv as ht
import test_acquisition as ta
import test_lml_optimizer as lo
import test_ase_api as taa
import test_learning_curve as tlc

from common import get_data

warnings.filterwarnings("ignore")

wkdir = os.getcwd()


class ConfigTestCase(unittest.TestCase):
    """Test suite for AtoML code base."""

    def test_ads_fp_funct(self):
        """Test adsorbate fingerprinting functions."""
        images = afp.setup_atoms()
        images = afp.attach_adsorbate_info(images)
        afp.ads_fp_gen(images)

    def test_bulk_fp_funct(self):
        images = bfp.setup_metal()
        bfp.bulk_fp_gen(images)

    def test_data_setup_func(self):
        """Test data setup routines."""
        # Test data setup functions.
        fb.feature_base_test()
        all_cand, data = ds.feature_test()
        ds.cv_test(data)
        ds.db_test(all_cand, data)

    def test_data_clean_func(self):
        """Test data cleaning routines."""
        dc.outlier_test()
        dc.variance_test()
        dc.inf_test()

    def test_feature_opt_func(self):
        """Test feature optimization routines."""
        ft.test_importance()
        train_features, train_targets, test_features = ft.test_extend()
        ft.test_extract(train_features, train_targets, test_features)
        ft.test_screening(train_features, train_targets, test_features)

    def test_lml_optimizer(self):
        """Test log_marginal_likelihood optimization."""
        train_features, train_targets, test_features, \
            test_targets = get_data()
        lo.lml_test(train_features, train_targets, test_features, test_targets)

    def test_acquisition_func(self):
        """Test acquisition routines."""
        train_features, train_targets, train_atoms, test_features, \
            test_targets, test_atoms = ta.get_data()
        ta.gp_test(train_features, train_targets, train_atoms,
                   test_features, test_targets, test_atoms)

    def test_hierarchy_func(self):
        """Test hierarchy routines."""
        ht.hierarchy_test()
        tlc.learning_curve_test()


if __name__ == '__main__':
    unittest.main()
    os.remove('{}/vec_store.sqlite'.format(wkdir))
