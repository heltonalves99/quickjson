import faker from 'faker';

const addFakeInterpolate = (value: string): string => {
  if (!value.includes('{{') && !value.includes('}}')) {
    return `{{${value}}}`;
  }
  return value;
};

const generateData = (valueList: any[]): string | string[] => {
  if (valueList[1]) {
    const values = [];
    for (let count = 0; count < (valueList[1] - 1); count += 1) {
      values.push(faker.fake(addFakeInterpolate(valueList[0])));
    }

    return values;
  }
  return faker.fake(addFakeInterpolate(valueList[0]));
};

const quickjson = (data: any) => {
  const result: any = {};

  Object.entries(data).forEach(([key, value]) => {
    result[key] = generateData(value as any);
  });
  return result;
};

export { quickjson };
