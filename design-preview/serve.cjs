const http = require('node:http');
const fs = require('node:fs');
const path = require('node:path');
const root = path.resolve(__dirname, '..');
const types = {'.html':'text/html; charset=utf-8','.css':'text/css; charset=utf-8','.js':'text/javascript; charset=utf-8','.webp':'image/webp','.png':'image/png','.jpg':'image/jpeg','.svg':'image/svg+xml','.ico':'image/x-icon','.woff2':'font/woff2','.mp4':'video/mp4','.webm':'video/webm','.json':'application/json'};
const server = http.createServer((request, response) => {
  try {
    const url = new URL(request.url, 'http://localhost');
    let pathname = decodeURIComponent(url.pathname);
    if (pathname === '/') pathname = '/index.html';
    if (pathname.endsWith('/')) pathname += 'index.html';
    const filename = path.resolve(root, '.' + pathname);
    if (!filename.startsWith(root + path.sep) || pathname.split('/').some(part => part.startsWith('.'))) {response.writeHead(403);return response.end('Forbidden');}
    fs.stat(filename, (error, stat) => {
      if (error || !stat.isFile()) {response.writeHead(404);return response.end('Not found');}
      const headers={'Content-Type':types[path.extname(filename)] || 'application/octet-stream','Cache-Control':'no-cache','Accept-Ranges':'bytes'};
      const range=request.headers.range?.match(/^bytes=(\d+)-(\d*)$/);
      if(range){const start=Number(range[1]),end=range[2]?Math.min(Number(range[2]),stat.size-1):stat.size-1;if(start>=stat.size||start>end){response.writeHead(416,{'Content-Range':`bytes */${stat.size}`});return response.end();}response.writeHead(206,{...headers,'Content-Range':`bytes ${start}-${end}/${stat.size}`,'Content-Length':end-start+1});return fs.createReadStream(filename,{start,end}).pipe(response);}
      response.writeHead(200, {...headers,'Content-Length':stat.size});
      fs.createReadStream(filename).pipe(response);
    });
  } catch {response.writeHead(400);response.end('Bad request');}
});
const port=Number(process.argv[process.argv.indexOf('--port')+1])||4173;
server.listen(port,'127.0.0.1',()=>console.log(`Shri Padmalaya: http://127.0.0.1:${port}/\nDesign collection: http://127.0.0.1:${port}/design-preview/`));
