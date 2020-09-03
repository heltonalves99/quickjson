import express from 'express';

const api = async (req: express.Request, res: express.Response) => {
  res.json({
    message: 'Test Here!',
  });
};

export { api as default };
