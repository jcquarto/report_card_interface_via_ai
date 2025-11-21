Rails.application.routes.draw do
  # Define your application routes per the DSL in https://guides.rubyonrails.org/routing.html

  # Defines the root path route ("/")
  root "report_cards#index"

  resources :report_cards, only: [:index, :show]
end
