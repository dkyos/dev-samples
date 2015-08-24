#!/bin/bash

./gradlew -q assemble

cd example
./gradlew -q tizenCreate
cd ..
