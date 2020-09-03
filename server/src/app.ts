import cors from 'cors';
import express, { Express } from 'express';
import morgan from 'morgan';
import helmet from 'helmet';

import api from './api';

import { notFound, errorHandler } from './app-middlewares';

export default function newApp(): Express {
  const app = express();
  app.use(cors());
  app.use(express.json());
  app.use(express.urlencoded({ extended: true }));
  app.use(morgan('common'));
  app.use(helmet());


  app.get('/', (req, res) => {
    res.json({
      message: 'Hello World!',
      user: 'Helton Alves',
    });
  });


  app.use('/api', api);

  app.use(notFound);
  app.use(errorHandler);

  return app;
}
