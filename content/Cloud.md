cloud enables
    rapid change - speed
    scale - scalability 
    resilience - agility
enabled by 
    ready to use cloud environment - pets vs cattle


12 factor (https://12factor.net/codebase)

1. codebase - one (version controlled) codebase per app. If apps share the codebase then move the common components to a common lib. 
2. For example, Bundler for Ruby offers the Gemfile manifest format for dependency declaration and bundle exec for dependency isolation. In Python there are two separate tools for these steps – Pip is used for declaration and Virtualenv for isolation.
3. configuration - The twelve-factor app stores config in environment variables (often shortened to env vars or env). Env vars are easy to change between deploys without changing any code; unlike config files, there is little chance of them being checked into the code repo accidentally; and unlike custom config files, or other config mechanisms such as Java System Properties, they are a language- and OS-agnostic standard.
4. Backing Services - The code for a twelve-factor app makes no distinction between local and third party services. To the app, both are attached resources, accessed via a URL or other locator/credentials stored in the config. A deploy of the twelve-factor app should be able to swap out a local MySQL database with one managed by a third party (such as Amazon RDS) without any changes to the app’s code. Likewise, a local SMTP server could be swapped with a third-party SMTP service (such as Postmark) without code changes. In both cases, only the resource handle in the config needs to change.
5. Build-Release-Run - Keep these steps separate. i.e. you can not make changes to code at run time and expect it to propagated back to build stage. *common sense*
6. Processes - execute using stateless processes which share nothing. The twelve-factor app never assumes that anything cached in memory or on disk will be available on a future request or job
7. Concurrency Twelve-factor app processes should never daemonize or write PID files. Instead, rely on the operating system’s process manager (such as systemd, a distributed process manager on a cloud platform, or a tool like Foreman in development) to manage output streams, respond to crashed processes, and handle user-initiated restarts and shutdowns.