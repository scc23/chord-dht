# Chord Distributed Hash Table

This program **chord-dht** is a Python implementation of a basic [Chord DHT](https://en.wikipedia.org/wiki/Chord_(peer-to-peer)), a protocol and algorithm for a peer-to-peer distributed hash table.

The main chord_dht.py implements the following functions:
- Initialize variables for DHT
- Initialize data for empty DHT with no nodes
- Insert node and key into DHT
- Compute finger table of node and associated query path

Included in the repository are two test cases **test.in** and **test2.in** that can be used to run the program for detailed outputs. 

![Image of Chord DHT](https://upload.wikimedia.org/wikipedia/commons/thumb/2/20/Chord_network.png/250px-Chord_network.png)
