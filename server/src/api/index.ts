import express from 'express';

import api from './controllers';

const router = express.Router();

export default router.get('/', api);
