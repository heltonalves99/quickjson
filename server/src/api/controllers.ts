import express from 'express';

import { quickjson } from '../utils';

const api = async (req: express.Request, res: express.Response) => {
  res.json({
    data: quickjson({
      user: ['name.findName'],
      email: ['internet.email'],
      imgs: ['image.image', 10],
      test: ['-- {{lorem.word}} - {{lorem.word}} --'],
    }),
  });
};

export { api as default };
