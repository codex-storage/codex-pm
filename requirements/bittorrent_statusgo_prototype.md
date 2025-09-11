# Codex prototype requirements

## Replacing BitTorrent with Codex in the Community History Service

The goal of the [community history
service](https://status.app/specs/status-community-history-service) in Status is
to ensure that messages older than 30 days are capable of being retrieved by
ephemeral community members. Currently, control nodes seed message archive
torrents to the BitTorrent network, and member nodes download the necessary
message archives using a magnet link. Codex will replace the use of the
BitTorrent network, by uploading datasets to Codex, and using CIDs for download
instead of magnet links.

### The current Community History Service

Every 7 days, [message
archives](https://status.app/specs/status-community-history-service#message-history-archives)
are created by community control nodes and appended to a blob of previous
archives. This blob, along with a [message history archive index
file](https://status.app/specs/status-community-history-service#message-history-archive-index)
("index file") containing metadata about the message archives in the blob, are
packaged into a single bundle for which a torrent is created and seeded on the
BitTorrent network. The [magnet link for this
bundle](https://status.app/specs/status-community-history-service#creating-magnet-links)
is distributed to community members over a [special, hidden, Status/Waku
channel](https://status.app/specs/status-community-history-service#message-archive-distribution).

When community members [first join the community, return online after some time
offline, or receive a live message history
update](https://status.app/specs/status-community-history-service#fetching-message-history-archives),
the latest magnet link is parsed from the special channel and any missing
message archives in the latest set of archives are downloaded. In effect,
message archives are replicated across all community member nodes.

### Codex's replacement of BitTorrent in the Community History Service

Codex must replace the use of the BitTorrent network in this process, which is
currently [implemented in
`status-go`](https://github.com/status-im/status-go/blob/6322f22783585474803cfc8a6f0a914757d763b5/protocol/messenger_communities.go#L3783).

To achieve this, the index file and all message archives will have their own CID
and will be uploaded to the Codex network separately. This differs from the
current implementation where the message archive bundle has [a single
torrent](https://status.app/specs/status-community-history-service#creating-message-archive-torrents)
and [magnet
link](https://status.app/specs/status-community-history-service#creating-magnet-links);
now, the index file and its constituent archives will be split out and uploaded
to the Codex network separately, each with their own CIDs.

The [design proposal](https://hackmd.io/SdVRXfnTQ_uedz_N7DeFqg) describes
distribution and download well:
> Instead of the magnet link, the community owner only publishes [the] `index`
CID [in the special channel].
>
> In order to receive the historical messages for the given period (given by
`from` and `to` in the `WakuMessageArchiveMetadata`), the receiving node first
acquires the `index` using the `index` CID. For each entry in the `index` that
the node has interest in, the node then downloads the corresponding archive
directly using the `Cid` from this `index` entry.
>
> The diagram below shows the relationship between the new `index` identified by
a Codex CID that uses individual CIDs to refer to each individual archive:

![team-nl-br-design-3](https://hackmd.io/_uploads/rJinDHHYge.svg)

### Assumptions

#### Node role

Node are assumed to be desktop nodes with enough space available to
download indices and message archives when they are received over the special
channel.

#### Message archive size

The size of the message archives will be dependent upon the activity in each
community. It remains unclear what a community's average message activity is and
consequently, the size of current message archives. However, an upper bound of
message archive size should be established.

It was reported that when the Community History Service was first implemented to
export Discord messages, the message archive was **10GB**, which we assume is
the upper bound of message archive dataset size because $i)$ the archive was not
limited to 7 days of Discord history (it was the *entire* history), $ii)$ the
community already had an established history on Discord compared to newer
communities on Status, and $iii)$ it stands to reason that usage on Discord was
greater than on Status due to platform network effect, different UX, and member
churn during the transition.

## FURPs requirements

It should be noted that these requirements represent a *prototype* of the
replacement of BitTorrent in the Community History Service only. These
requirements will need to be redefined as Codex moves away from a service to
Status and into its own protocol.

### Functionality

1. Ability to transfer datasets of at most 10GB between two or more nodes.
2. Datasets must be represented with a verifiable CID for data integrity.
3. Each community member must run a Codex node (free space should be verified on
   startup).
4. Providers of datasets must be discoverable by querying for a CID.
5. Uploaded or downloaded datasets must be downloadable by peers.
6. `index` files must have their own CID.
7. Message archive files must have their own CID.
8. [`WakuMessageArchiveIndexMetadata`](https://status.app/specs/status-community-history-service#wakumessagearchiveindex) must contain a CID of a message archive.

### Usability

1. Functionality to upload and download should be exposed over a REST API or
   available through Go-bindings.

### Reliability

1. Once a dataset is uploaded, the dataset should be retrievable by any
   member of the community.
2. Once a dataset is uploaded, at least one seeder of the dataset must remain
   online so the dataset is retrievable.

### Performance

1. As soon as a dataset is downloaded, there should be no delay in availability
   of the dataset to peers.

### Supportability

1. Nodes behind a NAT should be able to connect peers in a community.
