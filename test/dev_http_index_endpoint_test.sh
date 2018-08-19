#!/usr/bin/env bash

URL_INDEX="https://2wvhut15w3.execute-api.eu-west-1.amazonaws.com/dev"
TEST_RESULT="test_result_dev_index_endpoint.txt"
DIVIDER="\n=====================================================================\n"

touch $TEST_RESULT

# TEST 1

echo -e $DIVIDER > $TEST_RESULT

echo "TEST SCENARIO 1" >> $TEST_RESULT

echo "Benching: $URL_INDEX" >> $TEST_RESULT

echo "Testing 100 requests with concurrent 10" >> $TEST_RESULT

echo -e $DIVIDER >> $TEST_RESULT

ab -n100 -c10 $URL_INDEX >> $TEST_RESULT

# TEST 2

echo -e $DIVIDER >> $TEST_RESULT

echo "TEST SCENARIO 2" >> $TEST_RESULT

echo "Testing 1000 requests with concurrent 10" >> $TEST_RESULT

echo -e $DIVIDER >> $TEST_RESULT

ab -n1000 -c10 $URL_INDEX >> $TEST_RESULT

echo -e $DIVIDER >> $TEST_RESULT





