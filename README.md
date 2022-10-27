# lost_ootb_pipes
Out Of The Box pipelines for LOST image annotation tool

This repo is currently under construction!

## sia
### Description
Request single image annotations for all images of a specified data source.
### How do I use the pipeline ?
## mia
### Description
Request multi image annotations for all images of a specified data source.
### How do I use the pipeline ?
## sia_request_again
### Description
Request all annotations from a dataset file (csv or parquet) in lost_dataset format again.
### How do I use the pipeline ?

## mia_request_again
### Description
Request all annotations from a dataset file (csv or parquet) in lost_dataset format again.
### How do I use the pipeline ?

## two_stage
### Description
This pipeline represents a two stage annotation process. In a first stage bbox annotations are collected and in the second stage this bboxes will be labeled by MIA.

## mia_sia
### Description
In first stage use MIA to sort out images that are not of interest (e.g. empty images).
In second stage annotate the selected images from stage one with SIA.