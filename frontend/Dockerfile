FROM node:16-alpine

WORKDIR /app

# Copy package.json and package-lock.json
COPY package.json package-lock.json /app/

# Install dependencies
RUN npm install

# Copy the rest of the application
COPY . /app/

# Expose the port Vite runs on
EXPOSE 3000

# Command to run Vite
CMD ["npm", "run", "dev", "--", "--host"]

