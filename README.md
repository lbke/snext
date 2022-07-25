# Getting started with Snext

Snext is a Next.js application that lets you create API routes in Python.

Snext, because it sounds like "snake"🐍. You know, like a Python.

**/!\ /!\ /!\ This is an early experiment**

## Start with Python 🐍

Hey, if you end up there, you are probably a JavaScript developer and Python is only your second language. 

Here is how to setup an efficient Python environment.

### Install Python

I suggest using [Pyenv](https://github.com/pyenv/pyenv) to install Python. Consider it as an equivalent to Node Version Manager or Volta but for Python.

This is equivalent to using [Volta](https://volta.sh/) or [NVM](https://github.com/nvm-sh/nvm) in the Node ecosystem.

### Very first run: setup a virtual environment.

Python doesn't have a `node_modules` folder. That's maybe for the best, however it makes it quite hard to 
handle dependencies when you have a lot of projects on your machine.

A virtual environment is a bit similar: it will tell Python to install packages locally to your current project,
and not globally.

The difference with Node is that you must enable them systematically.

Setup a Virtual environment and install the Python packages:

```sh
python3 -m venv ./venv
source ./venv/bin/activate
pip install -r requirements.txt
```

### Subsequent runs

You need to activate the virtual env when you start working: 

```sh
source ./venv/bin/activate
```

**This command doesn't work in NPM scripts, sadly.** You have to type it everytime.

## Get started


## Various resources and inspirations

- Discussion on Vercel Github: https://github.com/vercel/vercel/discussions/4023
- Plotly Dash: one of the most impressive attempts at isomorphic web programming. Dash let's you use React components in Python to create interactive dashboards https://plotly.com/dash/
- Official doc about Python in Vercel: https://vercel.com/docs/runtimes#official-runtimes/python
- https://stackoverflow.com/questions/63190114/call-a-python-script-from-react-with-next-routing-and-a-node-js-server
- https://medium.com/swlh/build-a-twitter-login-component-using-nextjs-and-python-flask-44c17f057096
- https://github.com/vercel/next.js/discussions/15846

## TODO

- [X] Investigate how much `vercel` CLI can solve our issues (see [https://vercel.com/docs/cli#commands/dev](https://vercel.com/docs/cli#commands/dev)) => done, it does!
- [ ] Test local build
- [ ] Test vercel deployment
- [ ] Improve dev experience with Python, which is a bit more tedious than using JS (virtual env)?
- [ ] Build with `p

## Main blockers

### 1) Running 2 (or more) servers on the same port for Python and Node **SOLVED**

#### Solution:

Use Vercel CLI instead of `next dev`.

Vercel CLI command `vercel dev` is able to simulate a serverless environment locally, so you can test your API routes.

If you put all API routes in `./api/`, and use `vercel dev`, you can have both Python and Node.js API routes (and of course the Next.js frontend still works fine).

----

Read https://github.com/vercel/vercel/discussions/6197

#### Node + Python

When running Next, you'll want everything to run on `localhost:3000`, but you'll have 2 servers: one for Node, one for Python. This require some rewriting logic to work.

##### Possible solutions

- Check if Next.js rewrites in next.config.js already allow this
- Run a 3rd server that handles the redirection

##### Questions

- How is it solved in Next for API routes and frontend?

#### Python + Python

Also, we may have multiple API routes, that will act as serverless functions when deployed. But locally, we must make them one server.

##### Possible solutions

- We have a partial solution with Sanic Dispatcher, see "python-server.py". It rely on a main server, that dispatch the request to Sanic apps, so you have only one server and yet can run multiple API routes
- We still need to automate the import of relevant routes. Using a kind of Webpack-like magic, but in Python.
-  https://peterhaas-me.medium.com/how-to-run-multiple-flask-applications-from-the-same-server-9ca2c0ad7bb3
-  https://werkzeug.palletsprojects.com/en/1.0.x/middleware/dispatcher/
- Dispatcher for Sanic: https://github.com/ashleysommer/sanic-dispatcher/blob/master/sanic_dispatcher/extension.py#L131


### 2) Getting static data

The recommended pattern to get static data from you API routes in Next, is to reuse the core logic of the route directly in `getStaticProps`. But this is only possible because both are using JS. With Python, we would need to build the API routes first, run them, and then only build the frontend.

Needs to be tested with Vercel CLI.

### 3) Runtime failure

We have this error `https://github.com/vercel/community/discussions/103` in the latest version, the Python runtime seems too big.
See https://github.com/vercel/community/discussions/103#discussioncomment-1052162
See https://github.com/vercel/vercel/issues/2830

## Secondary issues

### Can't have vercel dev as the dev command

See https://github.com/vercel/vercel/blob/main/errors/now-dev-as-dev-script.md

The script must be named smth else for instance `dev:vercel` otherwise it creates an infinite loop.

### Underscore in Python folder names

No `-` in folder names in Python, or you're gonna have a bad time importing files... Use underscore `_`.
This may lead to messy URLs because the folder name is tied to the route name in Next.

#### Possible solutions

- Autogenerate a map of possible routes, or use URL rewriting

### What server to pick

(From my limited experience with Python) I'd tend to compare Flask or Falcon to Express: used a lot, minimal enough. But the blocking behaviour of Python can be very confusing to the JavaScript developer.
So I'll go for Sanic, because it relies on async/await like Node.js and might be the least confusing.

Anyway, all knowledge gathered for one framework should be reusable for any other framework.

### Setup Runtime for hosting

For simplification, we'll suppose a hosting on Vercel.
We may need a `vercel.json` to tell Vercel which runtime to use:
https://vercel.com/docs/runtimes#advanced-usage/community-runtimes

Since Vercel dev works, we should expect Vercel deployment to work out of the box. To be tested.

### The Virtual Env

In Python, you need a Virtual Environment to isolate your packages between apps, while in JS `node_modules` plays this role. The problem is that the virtual environment must be activated when you start working, so that's an additional step for the developer.
To make it worse, the `source` command that activate the environment cannot be (last time I've checked) put in `package.json`, so you have to remember the right command everytime.

---

## About Next

This is a [Next.js](https://nextjs.org/) project bootstrapped with [`create-next-app`](https://github.com/vercel/next.js/tree/canary/packages/create-next-app).

## Getting Started

First, run the development server:

```bash
npm run dev
# or
yarn dev
```

Open [http://localhost:3000](http://localhost:3000) with your browser to see the result.

You can start editing the page by modifying `pages/index.js`. The page auto-updates as you edit the file.

[API routes](https://nextjs.org/docs/api-routes/introduction) can be accessed on [http://localhost:3000/api/hello](http://localhost:3000/api/hello). This endpoint can be edited in `pages/api/hello.js`.

The `pages/api` directory is mapped to `/api/*`. Files in this directory are treated as [API routes](https://nextjs.org/docs/api-routes/introduction) instead of React pages.

## Learn More

To learn more about Next.js, take a look at the following resources:

- [Next.js Documentation](https://nextjs.org/docs) - learn about Next.js features and API.
- [Learn Next.js](https://nextjs.org/learn) - an interactive Next.js tutorial.

You can check out [the Next.js GitHub repository](https://github.com/vercel/next.js/) - your feedback and contributions are welcome!

## Deploy on Vercel

The easiest way to deploy your Next.js app is to use the [Vercel Platform](https://vercel.com/new?utm_medium=default-template&filter=next.js&utm_source=create-next-app&utm_campaign=create-next-app-readme) from the creators of Next.js.

Check out our [Next.js deployment documentation](https://nextjs.org/docs/deployment) for more details.
