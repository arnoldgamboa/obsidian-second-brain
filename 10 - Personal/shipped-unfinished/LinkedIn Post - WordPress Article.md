---
tags: [linkedin, social, wordpress, agency, astro]
date: 2026-04-29
---

# LinkedIn Post — Why I Won't Build Your Website in WordPress

I got a call at 11:03 PM last year.

A client's website was showing a phishing page in Chinese. Every URL redirected to a fake login screen. His customers were messaging him, panicked.

An outdated contact form plugin — installed because it was "free" — had a known vulnerability. The attacker automated the exploit and dropped a backdoor.

Four hours to clean. Two days to harden. The client didn't sleep that night. Neither did I.

---

I've used WordPress for 15 years. I'm not saying it's a bad tool. I'm saying it's the wrong default for business-critical sites.

The average business WordPress site has 15-30 plugins. Each is someone else's code running on your server. Each has its own update cycle and security surface. The client sees a free feature. I see a support ticket waiting to happen.

"Free" WordPress is often the most expensive option over three years:
- Premium plugin renewals
- Managed hosting to handle bloat
- Security monitoring
- A developer on call
- Emergency cleanup when it breaks

Meanwhile, the site scores 34 on PageSpeed because of plugins the client never asked for.

---

What I use instead for most agency clients:

Astro + a headless CMS (Sanity or Strapi).

HTML pages. Zero JavaScript by default. 95+ PageSpeed out of the box. Hosting costs $0-20/month. No database on the public server. No plugin ecosystem to maintain.

I've rebuilt three WordPress sites on this stack. Hosting bills dropped 70-80%. Support tickets went from monthly to zero.

WordPress still makes sense for blogs, hobby sites, and projects under $5K. But if your site is business-critical, defaulting to WordPress is a gamble I no longer take with a client's money.

---

Wrote a longer post about the full stack breakdown — when WordPress works, when it doesn't, and what to use instead:

https://arnold.gamboa.ph/why-i-wont-build-your-website-in-wordpress-and-what-i-recommend-instead/

#webdevelopment #agencylife #wordpress #astro #headlesscms #digitalagency
