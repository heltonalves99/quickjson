import {
  Request,
  Response,
  NextFunction,
} from 'express';

interface ResponseError extends Error {
  status?: number;
}

export const notFound = (req: Request, res: Response, next: NextFunction) => {
  const error = new Error(`Not Found - ${req.originalUrl}`);
  res.status(404);
  next(error);
};

// eslint-disable-next-line
export const errorHandler = (error: ResponseError, req: Request, res: Response, next: NextFunction) => {
  res.status(res.statusCode || 500);
  res.json({
    message: error.message,
    stack: process.env.NODE_ENV === 'prod' ? '' : error.stack,
  });
};
