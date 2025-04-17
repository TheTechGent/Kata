#include <SDL.h>
#include <iostream>

// CONSTANTS
const int WINDOW_HEIGHT;
const int WINDOW_WIDTH;
const int PADDLE_HEIGHT;
const int PADDLE_WIDTH;
const int PADDLE_SPEED;
const int BALL_SIZE;
const int BALL_SPEED;

struct Paddle
{
	SDL_Rect rect;
	int speed;
};

struct Ball
{
	SDL_Rect rect;
	int VelX, VelY;
};

void HandleInput(bool& running, Paddle& leftPaddle, Paddle& rightPaddle);
void Update(Ball& ball, Paddle& leftPaddle, Paddle& rightPaddle);
void Render(SDL_Renderer* renderer, const Ball& ball, const Paddle& leftPaddle, const Paddle& rightPaddle);

int main(int argc, char* argv[])
{
	// Initialise SDL

	if (SDL_Init(SDL_INIT_VIDEO) < 0)
	{
		std::cerr << "SDL Initialise failed" << SDL_GetError() << std::endl;
	}

	// Create SDL Window
	
	SDL_Window* window = SDL_CreateWindow(
		"Pong", 
		SDL_WINDOWPOS_CENTERED, 
		SDL_WINDOWPOS_CENTERED, 
		WINDOW_WIDTH, 
		WINDOW_HEIGHT, 
		SDL_WINDOW_SHOWN
	);

	return 0;
}



void HandleInput(bool& running, Paddle& leftPaddle, Paddle& rightPaddle)
{
}

void Update(Ball& ball, Paddle& leftPaddle, Paddle& rightPaddle)
{
}

void Render(SDL_Renderer* renderer, const Ball& ball, const Paddle& leftPaddle, const Paddle& rightPaddle)
{
}
