#!/bin/sh
npm install --force
npm run build
exec npm run start