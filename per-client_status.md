# Per-Client statuses

Discord serves a "simple" `status` field in presence update objects. Recently
they added a `client_status` that gives other users the ability to get
per-client status information.

Setting a client status happens with the same known logic, via
OP 3 Status Update in the Gateway API. Discord knows the currently connected
client via the Connection Properties. From there they dispatch Presence Update
events to other users containing the `client_status` field.

## ClientStatus object

| field | type | description |
| --: | :-- | :-- |
| mobile | Optional[Status] | mobile client status |
| desktop | Optional[Status] | desktop client status |
| web | Optional[Status] | web client status |
