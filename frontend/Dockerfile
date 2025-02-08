# Step 1: Use an official Node.js image
FROM node:16

# Step 2: Set the working directory inside the container
WORKDIR /frontend

# Step 3: Copy package.json and package-lock.json
COPY package.json package-lock.json ./

# Step 4: Install dependencies
RUN npm install

# Step 5: Copy the rest of the React app's source code
COPY . .

# Step 6: Expose the port that the React app will run on
EXPOSE 3000

# Step 7: Start the React app using npm start
CMD ["npm", "start"]
