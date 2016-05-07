
# Create hash to use in R like a python dictionary
hash_list <- function(vars, names) {
  
  if(!length(vars) == length(names)) {
    stop("Length of two vectors is not equal! Abort.")
  }
  
  N <- length(vars) 
  mylist <- vector('list', N) 
  for (i in 1:N) { 
    mylist[[vars[i]]] =  names[i]
  } 
  
  return(mylist)
}
