# Discord's Internal Infrastructure

Taken off [discord-infra](https://gitdab.com/luna/discord-infra/src/branch/master/internals.md).

## Disclaimer

This has some degree of speculation as Discord's backend is closed.

[cassandra]: https://cassandra.apache.org
[mongodb]: https://www.mongodb.com
[flask]: http://flask.pocoo.org
[punt]: https://github.com/discordapp/punt
[loqui]: https://github.com/discordapp/loqui
[webrtc]: https://webrtc.org/
[scylla]: https://scylladb.com/
[grpc]: https://grpc.io/

## Storage:

- [Scylla] for storage
  - They used [Cassandra] for such but that [changed](https://www.scylladb.com/press-release/discord-chooses-scylla-core-storage-layer/)
  - They used [MongoDB] as primary storage, but moved to Cassandra,
    [source](https://blog.discordapp.com/how-discord-stores-billions-of-messages-7fa6ec7ee4c7)).
- It is still unknown what role MongoDB has on the stack, but it is still
  a primary part of the service: [source](https://status.discordapp.com/incidents/rkj7rx8f4865)
  and [source](https://status.discordapp.com/incidents/2cb5jc53jq28).

## Programming languages:

- [Elixir](https://elixir-lang.org/) for the Gateway/WebSockets API,
  [source](https://blog.discordapp.com/scaling-elixir-f9b8e1e7c29b).
  - [ex_hash_ring](https://github.com/discordapp/ex_hash_ring)
  - [manifold](https://github.com/discordapp/manifold)
  - [fastglobal](https://github.com/discordapp/fastglobal)
  - [semaphore](https://github.com/discordapp/semaphore)
  - [instruments](https://github.com/discordapp/instruments)
  - [deque](https://github.com/discordapp/deque)
  - [Use of GenStage](https://blog.discordapp.com/how-discord-handles-push-request-bursts-of-over-a-million-per-minute-with-elixirs-genstage-8f899f0221b4)
- [Python](https://www.python.org/) for HTTP/REST API,
  The best guesses to which framework are [Flask].
- [Go](https://golang.org):
  - The embed servers, confirmed by Discord developers _informally_.
  - Note that the embedding servers and mediaproxy, while able to be its
    own logical unit, as experimented in litecord's [mediaproxy], can
    be treated separately.
  - [Punt], replacing Logstash in ELK (Elasticsearch, Logstash, Kibana) setups.
  - [Lilliput](https://github.com/discordapp/lilliput), which is a main part
    of their media proxy. Lillput is also written in C++.
    [source](https://blog.discordapp.com/how-discord-resizes-150-million-images-every-day-with-go-and-c-c9e98731c65d)
- [Rust](https://www.rust-lang.org/) for parts of the Discord Store, most commonly:
  - [GameSDK](https://discordapp.com/developers/docs/game-sdk/sdk-starter-guide),
    to make Discord integrations for any game.
  - [Dispatch](https://discordapp.com/developers/docs/dispatch/dispatch-and-you),
    which is a tool to send assets to Discord's servers.
  - It is known Rust is used for lazy guilds. [source](https://blog.discordapp.com/using-rust-to-scale-elixir-for-11-million-concurrent-users-c6f19fc029d3)
  - Read States service, rewritten from Go. [source](https://blog.discordapp.com/why-discord-is-switching-from-go-to-rust-a190bbca2b1f)
- C++ for the [Discord RPC library](https://github.com/discordapp/discord-rpc). (deprecated in favor of GameSDK)

## Distribution:

- [gRPC] for node communication.
  - They used their own, [Loqui], but [that changed](https://github.com/discord/loqui/commit/8d394a7951fd3a82d109becc1aebbd9e7ccc894a).

## Logging:

- [Punt] in favour of [Logstash](https://github.com/elastic/logstash) for logging.
- [Elasticsearch](https://github.com/elastic/elasticsearch) that powers the search feature for users and powers logging.
  - Sources about logging: Punt and [this issue](https://github.com/elastic/elasticsearch/issues/20354)
  - [Source about message search](https://blog.discordapp.com/how-discord-indexes-billions-of-messages-e3d5e9be866f)

## External services

- [Google's Cloud Platform](https://cloud.google.com/) for their infrastructure,
  [source](https://status.discordapp.com/incidents/rhvp2tn7g0zc)
- [Cloudflare](https://www.cloudflare.com/) as a proxy to almost all services,
  voice servers need to be direct connections, so they don't pass through CF.
  More on voice servers in the WebRTC source.
- "[...]we use [Algolia](https://www.algolia.com/) to power some search features at Discord."
  [source, by jhgg](https://news.ycombinator.com/item?id=23719172)

## General technologies

- [WebRTC] for voice and video. [Source](https://blog.discordapp.com/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429),
  which also goes on more detail on how the voice server architecture works.

## Many other sources

- [Description of a full outage where they had to reboot everything](https://status.discordapp.com/incidents/dj3l6lw926kl)
- [`sessions` and `presence` clusters get rebooted due to a host error in a `guild` node](https://status.discordapp.com/incidents/ywdwttd6b0hg)
- [Repeating message sends due to errors in the `push` cluster](https://status.discordapp.com/incidents/93kyyctg0wf3)
- ["furiously" spinning an nginx cluster due to an error in GCP's load balancer](https://status.discordapp.com/incidents/rhvp2tn7g0zc)
