# Apache Avro Alert Schema

Apache Avro uses a schema to structure the data (define data types and protocols) that is being encoded (compact binary format). It has two different types of schema languages: one for human editing (Avro IDL) and another which is more machine-readable based on (JSON).


## ZTF alert schema timeline

The ZTF alert schema evolves over time, to include the latest information. We provide a sample alert for each version (starting in 2019) in this folder: `template_schema_ZTF_<version>.avro`. One can find the latest description of fields on this [page](https://zwickytransientfacility.github.io/ztf-avro-alert/).

| Period | Schema version | Change |
|:--------|:-------|:-------|
| Jul 2018 - Jan 2019 | version 3.1 | -- |
| Jan 2019 - Jul 2019 | version 3.2 | [commit](https://github.com/ZwickyTransientFacility/ztf-avro-alert/commit/2b4af549fc99200e3117c24634a17b5ac04ed963) |
| Jul 2019 - now | version 3.3 | [commit](https://github.com/ZwickyTransientFacility/ztf-avro-alert/commit/a4fa6a45621ccfc11e7a38f766a05c63681fd4e3#diff-c9550d5fad73447fc24ba47f95d1c6b7) |

## Fink Distribution schema [ZTF]

The Fink distribution schema is the input ZTF alert schema plus additional fields describing the added values by Fink. This schema is mandatory to decode the alerts receive by the Fink client, and we release schema versions in this folder: `distribution_schema_<version>.avsc`. The fields are described on this [page](https://fink-broker.readthedocs.io/en/latest/science/added_values/).

| Period | Schema version | Commit | Added values |
|:--------|:-------|:-------|:-------|
| Jul 2019 - Jan 2020 | version 0.1 | -- | `cdsxmatch` |
| Jan 2020 - now | version 0.2 | [commit](https://github.com/astrolabsoftware/fink-broker/commit/bc5a03ae42513841c8c071a49f17bae1978e0e94) | `rfscore` |

## Simulator vs live streams

We run Fink in two modes: live (i.e. live data from ZTF), or simulation (replayed
streams using the Fink alert simulator). While we would expect the schema to be the same,
there are some small variations due to the way Spark handles input schema. The variations are as small as some missing comments in the schema - but nevertheless sufficient for the client to consider the data from live or simulation to need a different schema... Hence, for each schema version, we have two files:

```
schema_name_XpY.avsc --> suitable for data from simulator
schema_name_XpY-live.avsc --> suitable for live data
```

We intend to find a solution to merge the two in the future.

# Construction of the Fink oriented schema.

This is the Avro schema meant to describe the alerts based on telescope source, augmented with the various Fink science modules

Every contribution of the Fink schema is assigned a version id (incuding the telescope one, which is provided by the telescope itself).
The assembled Fink schema receives a Fink version id and described n the ``Fink_M.m.conf`` file.

Contributions exist as source/<name>_M.m.avsc files

