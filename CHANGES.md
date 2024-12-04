# CHANGELOG

## b2btest 1.4.2 (2024-12-04)

- Solved warnings on deprecated `pkg_resources`
- CI for all supported Python versions including 2.7
- Documentation updated: where to find diff plugins for pdf and audio

## b2btest 1.4.1 (2023-09-11)

- back2back.py: accepts specific cases to run as argument
- CI fixed

## b2btest 1.4.0 (2022-01-02)

- Audio plugin separated from this code base as `b2btest_audio`
	- This removes dependencies for most common cases that do not need audio
- Removed all assertEquals (with 's')
- CI: Travis -> Github

## b2btest 1.3.3 (2019-11-15)

- Simplified dependency on lxml

## b2btest 1.3.2 (2019-11-15)

- `diffaudio` as console script
- `diffxml` as console script
- Fix: entry points for xml and audio plugins
- Just markdown README

## b2btest 1.3.1 (2019-10-04)

- Updated README

## b2btest 1.3 (2019-10-04)

- Avoid large diffs by telling just the generated file with the failed results
- Fix unicode problems in certain python versions
- Using older lxml versions for python<3.5

## b2btest 1.2 (2016-03-23)

- CLI: Fix: only the first output was actually checked
- Plugin based type sensitive diff
- Specific diff for XML
- XML and Audio diffing now are extras
- 'extensions' key in yaml testcases to associate custom file extensions to a diff plugin

## b2btest 1.1 (2016-03-12)

- Unit test like usage for back-to-back test Python code instead of command line programs.
- New commandline tool `back2back` that takes a yaml file with the test cases definitions.

## b2btest 1.0 (2013-01-03)

- First github version
- (There were previous unpublished versions)


