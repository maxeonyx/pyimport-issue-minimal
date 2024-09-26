retry(do_thing)

# Uncomment the above line and take the suggested import actions.
#
# You will get an incorrect import for the shared module. There are intermediate
# paths (notably the workspace root) which are not on the pythonpath:
#
# from ...depsrc.sharedmodule.patterns import retry
#
# When run with the following command, we will get "ImportError: attempted
# relative import beyond top-level package":
#
# PYTHONPATH=appsrc:depsrc python -m appmodule

# If we change "python.analysis.importFormat" to "absolute", then our local
# import will be absolute.
