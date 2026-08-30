const http = require('http');
function handler(req, res) {
  const u = new URL(req.url, 'http://localhost');
  const expr = u.searchParams.get('expr');
  const result = eval(expr);
  res.end('result ' + result);
}
http.createServer(handler);
module.exports = { handler };
