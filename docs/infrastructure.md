# Discord's Internal Infrastructure

Taken off [discord-infra](https://gitdab.com/luna/discord-infra/src/branch/master/internals.md).

## Disclaimer

This has some degree of speculation as Discord's backend is closed.


[Cassandra]: https://cassandra.apache.org
[MongoDB]: https://www.mongodb.com
[Flask]: http://flask.pocoo.org
[Punt]: https://github.com/discordapp/punt
[Loqui]: https://github.com/discordapp/loqui
[WebRTC]: https://webrtc.org/


## Storage:
 - [Cassandra](http://cassandra.apache.org/) for storage
 - They used [MongoDB] as primary storage, but moved to Cassandra,
    [source](https://blog.discordapp.com/how-discord-stores-billions-of-messages-7fa6ec7ee4c7)).
 - It is still unknown what role MongoDB has on the stack, but it is still
    a primary part of the service: [source](https://status.discordapp.com/incidents/rkj7rx8f4865)
    and [source](https://status.discordapp.com/incidents/2cb5jc53jq28).


## Programming languages:
 - [Elixir](https://elixir-lang.org/) for any real time communication,
    [source](https://blog.discordapp.com/scaling-elixir-f9b8e1e7c29b).
    - [ex\_hash\_ring](https://github.com/discordapp/ex_hash_ring)
    - [manifold](https://github.com/discordapp/manifold)
    - [fastglobal](https://github.com/discordapp/fastglobal)
    - [semaphore](https://github.com/discordapp/semaphore)
    - [instruments](https://github.com/discordapp/instruments)
    - [deque](https://github.com/discordapp/deque)
    - [Use of GenStage](https://blog.discordapp.com/how-discord-handles-push-request-bursts-of-over-a-million-per-minute-with-elixirs-genstage-8f899f0221b4)
 - [Python](https://www.python.org/) for HTTP/REST API,
    The best guesses to which framework are [Flask].
 - [Go](https://golang.org):
    - The embed servers, no *formal* source, but it has been confirmed by
        Discord developers informally.
    - Note that the embedding servers and mediaproxy, while able to be its
        own logical unit, as experimented in litecord's [mediaproxy], can
        be treated separately.
    - [Punt], replacing Logstash in ELK (Elasticsearch, Logstash, Kibana) setups.
    - [Lilliput](https://github.com/discordapp/lilliput), which is a main part
        of their media proxy. Lillput is also written in C++.
        [source!](https://blog.discordapp.com/how-discord-resizes-150-million-images-every-day-with-go-and-c-c9e98731c65d)
 - [Rust](https://www.rust-lang.org/) for many parts of the Discord Store, most commonly:
   - [Game SDK](https://discordapp.com/developers/docs/game-sdk/sdk-starter-guide),
        to make Discord integrations for any game.
   - [Dispatch](https://discordapp.com/developers/docs/dispatch/dispatch-and-you),
        which is a tool to send assets to Discord's servers.
 - C++ for the [Discord RPC library](https://github.com/discordapp/discord-rpc).


## Distribution:
 - [Loqui] for node communication.


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


## General technologies
 - [WebRTC] for voice and video. [Source](https://blog.discordapp.com/how-discord-handles-two-and-half-million-concurrent-voice-users-using-webrtc-ce01c3187429),
    which also goes on more detail on how the voice server architecture works.


## Many other sources
 - [Description of a full outage where they had to reboot everything](https://status.discordapp.com/incidents/dj3l6lw926kl)
 - [`sessions` and `presence` clusters get rebooted due to a host error in a `guild` node](https://status.discordapp.com/incidents/ywdwttd6b0hg)
 - [Repeating message sends due to errors in the `push` cluster](https://status.discordapp.com/incidents/93kyyctg0wf3)
 - ["furiously" spinning an nginx cluster due to an error in GCP's load balancer](https://status.discordapp.com/incidents/rhvp2tn7g0zc)
