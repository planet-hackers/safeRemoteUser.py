# safeRemoteUser.py
## Usage
`safeRemoteUser.py [user] [safe_remote1,safe_remote2]`

`[user]` - The user to check for pseudoterminal slaves

`[safe_remote1,safe_remote2]` - List of addresses from which the user is allowed to have a pseudoterminal slave

## Real life usage example
_This assumes you don't have root access to configure iptables_

You have a server on which multiple people connect by ssh using the same user.

The ssh server creates pseudoterminal slaves for each connection.

Use safeRemoteUser.py to specify all addresses from which a user can connect.
