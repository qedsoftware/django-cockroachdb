import os
import sys

# This file assumes it is being run in the django/tests/ repo.

enabled_test_apps = [
    'admin_changelist',
    'admin_custom_urls',
    'admin_docs',
    'admin_filters',
    'admin_inlines',
    'admin_ordering',
    'admin_utils',
    'admin_views',
    'aggregation',
    'aggregation_regress',
    'annotations',
    'auth_tests',
    'backends',
    'basic',
    'bulk_create',
    'cache',
    'check_framework',
    'conditional_processing',
    'constraints',
    'contenttypes_tests',
    'custom_columns',
    'custom_lookups',
    'custom_managers',
    'custom_methods',
    'custom_migration_operations',
    'custom_pk',
    'datatypes',
    'dates',
    'datetimes',
    'db_functions',
    'db_typecasts',
    'db_utils',
    'defer',
    'defer_regress',
    'delete',
    'delete_regress',
    'distinct_on_fields',
    'empty',
    'expressions',
    'expressions_case',
    'expressions_window',
    'extra_regress',
    'field_defaults',
    'field_subclassing',
    'file_storage',
    'file_uploads',
    'filtered_relation',
    'fixtures',
    'fixtures_model_package',
    'fixtures_regress',
    'force_insert_update',
    'foreign_object',
    'forms_tests',
    'from_db_value',
    'generic_inline_admin',
    'generic_relations',
    'generic_relations_regress',
    'generic_views',
    'get_earliest_or_latest',
    'get_object_or_404',
    'get_or_create',
    'i18n',
    'indexes',
    'inline_formsets',
    'inspectdb',
    'introspection',
    'invalid_models_tests',
    'known_related_objects',
    'lookup',
    'm2m_and_m2o',
    'm2m_intermediary',
    'm2m_multiple',
    'm2m_recursive',
    'm2m_regress',
    'm2m_signals',
    'm2m_through',
    'm2m_through_regress',
    'm2o_recursive',
    'managers_regress',
    'many_to_many',
    'many_to_one',
    'many_to_one_null',
    'max_lengths',
    'migrate_signals',
    'migrations',
    'migration_test_data_persistence',
    'modeladmin',
    'model_fields',
    'model_forms',
    'model_formsets',
    'model_formsets_regress',
    'model_indexes',
    'model_inheritance',
    'model_inheritance_regress',
    'model_meta',
    'model_options',
    'model_package',
    'model_regress',
    'multiple_database',
    'mutually_referential',
    'nested_foreign_keys',
    'null_fk',
    'null_fk_ordering',
    'null_queries',
    'one_to_one',
    'ordering',
    'order_with_respect_to',
    'or_lookups',
    'pagination',
    'prefetch_related',
    'properties',
    'proxy_model_inheritance',
    'proxy_models',
    'queries',
    'queryset_pickle',
    'raw_query',
    'reserved_names',
    'reverse_lookup',
    'save_delete_hooks',
    'schema',
    'select_for_update',
    'select_related',
    'select_related_onetoone',
    'select_related_regress',
    'serializers',
    'servers',
    'signals',
    'sitemaps_tests',
    'sites_framework',
    'sites_tests',
    'string_lookup',
    'swappable_models',
    'syndication_tests',
    'test_client',
    'test_client_regress',
    'test_utils',
    'timezones',
    'transaction_hooks',
    'transactions',
    'unmanaged_models',
    'update',
    'update_only_fields',
    'validation',
    'view_tests',
]

run_tests_cmd = "python3 runtests.py %s --settings cockroach_settings -v 2"

shouldFail = False
for app_name in enabled_test_apps:
    res = os.system(run_tests_cmd % app_name)
    if res != 0:
        shouldFail = True

res = os.system("python3 runtests.py gis_tests --settings cockroach_gis_settings -v 2")
if res != 0:
    shouldFail = True

sys.exit(1 if shouldFail else 0)
