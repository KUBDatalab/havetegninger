library(reticulate)
reticulate::py_install("numpy")
reticulate::py_install("opencv-python")
reticulate::use_virtualenv("c:/users/cbk/documents/.virtualenvs/r-reticulate", required = TRUE)
