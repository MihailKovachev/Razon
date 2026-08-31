---
title: Users
tags:
    - linux
    - system-internals
    - computer-science
---

# Introduction

>[!DEFINITION] Definition: User
>
>A **user** in [[./index|Linux]] is an abstraction for keeping track of three things:
>- permissions - what *can* be done and by *whom*;
>- accountability - *who* is doing what;
>- ownership - who *owns* what.
>

We can logically divide users into three types: 
- The **Superuser** `root` is the most powerful user and is present on every [[./index|Linux]] system. It is allowed to do pretty much anything.
- **Regular users** usually correspond to real people. For example, there could be a user `bob` for your colleague Bob or a user `alice` for your manager Alice.
- **System users** are low-privileged users which are created for performing very specific tasks. For example, there could be a `db` user for managing databases. This "division of labor" enhances security.

Users can start [[TODO|processes]], and own [[TODO|files]] and [[TODO|directories]]. Furthermore, users can be added to [[TODO|groups]] to share permissions.

# Representation

User information is stored in the plain-text `/etc/passwd` file. Each line represents one user and has the following format:

```
username:password:UID:GID:GECOS:home:shell
```

- The `username` field contains the user's name. It is unique for every user.
- The `password` field used to contain the [[TODO|hash]] of the user's password. Nowadays, it contains either an asterisk (`*`) or the letter `x`, while the [[TODO|hash]] itself is stored in the `/etc/shadow` file. This is because the `/etc/passwd` file is meant to be readable by anyone and exposing password [[TODO|hashes]] is never a good idea. The `/etc/shadow` file, on the other hand, is only readable by the [[Users#Introduction|superuser]] `root`.
- The `UID` (user ID) field is a non-negative integer which is unique to each user. The UID 0 is reserved for the [[Users#Introduction|superuser]] `root` and UIDs in the range 1-999 are reserved for [[Users#Introduction|system users]]. This means that the UIDs of [[Users#Introduction|regular users]] usually begin at 1000 and onwards.
- Every user must belong to at least one [[Groups|group]], known as their **primary group**, and the [[Groups|ID]] of this [[Groups|group]] is stored in the `GID` (primary group ID) field.
- The `GECOS` field is often called the **comment field** and serves a purely informational purpose. It is usually used for the full name of the person behind the user, but can contain pretty much anything else, too.
- A user can have a default [[TODO|directory]] assigned to them where they can store their files. This is known as their **home directory** and the `home` field contains the [[TODO|absolute path]] to it. The `home` field is also used to set the `HOME` [[TODO|enviroment variable]].
- A user can also have a default [[../Shells|shell]] assigned to them which is used when they log in. The `shell` field contains the [[TODO|absolute path]] to this [[../Shells|shell]] and is also used to set the value of the `SHELL` [[TODO|environment variable]]. [[Users|System users]] usually do not have a default [[../Shells|shell]] and their `shell` field is either empty or the ends in `nologin` or `false`.

>[!EXAMPLE]- Example: Typical `/etc/passwd` File
>
>A typical `/etc/passwd` looks like this:
>
>![[res/Typical etc passwd File.png]]
>

Furthermore, each user also has a corresponding line in the `/etc/shadow` file. This file should only be readable by the [[Users#Introduction|superuser]] `root` because it contains sensitive information such as the [[TODO|hash]] of the password of each user. Every line has the following format:

```
username:hash:last_changed:min_password_age:max_password_age:password_warning_period:password_inactivity_period:account_expiration_date:reserved
```

- The `username` field contains the user's name.
- The `hash` field contains the [[TODO|hash]] of the user's password. If empty, then the user has no password. Note that many applications refuse to operate if the user has no password. If this field contains `*` or `!`, then password login is disabled for this user.
- The `last_changed` field contains the date of the last time the password was changed. It is expressed as the number of days since Jan 1, 1970 00:00 UTC. A value of 0 means that the user should change their password the next time they log in. If this field is empty, then password aging features are disabled.
- The `min_password_age` field stores the number of days the user has to wait after a password change before they can change their password again. A value of 0 indicates that the user does not have to wait at all.
- The `max_password_age` field is the number of days is the number of days since the last password change after which the password will expire and the user will be asked to change their password again. An empty field indicates that there is no such period, no password warning period and no password inactivity period. If `max_password_age` is lower than `min_password_age`, then the user is unable to change their password. 
- The `password_warning_period` is the number of days before the password expires during which the user will be warned that their password will soon expire. An empty field and a value of 0 indicate a lack of such a period.
- The `password_inactivity_period` is the number of days after the password expires during which it should still be accepted. Once the password has expired and this period has passed, the user can no longer log in with their password. An empty field means that such a period is not enforced and is essentially indefinite.
- The `account_expiration_date` is the date of expiration of the user. It is expressed in number of days since Jan 1, 1970 00:00 UTC. After this date, the user cannot login at all. A value of 0 can be interpreted either as an account with no expiration or as an account with an expiration date of Jan 1, 1970.
- The `reserved` field is reserved for future use.

>[!EXAMPLE]- Example: Typical `/etc/shadow` File
>
>A typical `/etc/shadow` file looks like this:
>
>![[res/Typical etc shadow File.png]]
>

# Sources

1. [passwd(5) - Linux manual page](https://man7.org/linux/man-pages/man5/passwd.5.html)
2. [shadow(5) - Linux manual page](https://man7.org/linux/man-pages/man5/shadow.5.html)