# kafka-python
Dummy project to test kafka with python


# Prerequisite

https://www.confluent.io/blog/introduction-to-apache-kafka-for-python-programmers/

### Install the librdkafka shared library and corresponding C header files
    brew install librdkafka

### Install python packages
    python3 -m vevn venv
    source venv/bin/activate
    pip install -r requirements.txt

# Start kafka single node

https://github.com/confluentinc/cp-docker-images/tree/4.0.x/examples

    docker-compose up -d
    docker-compose logs --tail=50 -f

# Run examples

    cd v1/
    python3 consumer.py
    python3 producer.py
