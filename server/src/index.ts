import dotenv from 'dotenv';

import newApp from './app';

const app = newApp();
dotenv.config();

const PORT = process.env.APP_PORT;
app.listen(PORT, () => {
  console.log(`Listening on http://localhost:${PORT}...`);
});
