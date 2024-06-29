from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """

    # Implement search here!
    
    returnList = []
    
    """ Easier Challenge
    
    # Set the parameters to None if not specified
    if 'id' not in args.keys():
        argId = None
    else:
        argId = args['id']
        
    if 'name' not in args.keys():
        argName = None
    else:
        # Apply lower case to standardize the data 
        # and make this argument case insensitive
        argName = args['name'].lower()
        
    if 'age' not in args.keys():
        argAgeRange = None
    else:
        # Make the age argument to range.
        argAgeRange = range(int(args['age'])-1, int(args['age'])+2)
        
    if 'occupation' not in args.keys():
        argOcc = None
    else:
        argOcc = args['occupation'].lower()
    for n in USERS:
        
        # Since the specification said that
        # "The user can also pass multiple parameters and the function should
        # return all the users that match ANY of the parameters provided."
        # Check for all the arguments. Append and continue to prevent duplicates as much as possible
        
        if argId is not None and n['id'] == argId:
            returnList.append(n)
            continue
        
        if argAgeRange is not None and n['age'] in argAgeRange:
            returnList.append(n)
            continue
            
        if argName is not None and argName in n['name'].lower():
            returnList.append(n)
            continue
        
        if argOcc is not None and argOcc in n['occupation'].lower():
            returnList.append(n)
            continue
    """
    
    # Use dict.keys() to make a list of keys in the proper order
    # Iterate on the keys
    # Iterate on the items
    # Add if blocks to satisfy special requirement per key
    
    # Create a different list
    # To prevent duplicates, remove the items already in the return list
    remainingList = USERS
    
    for key in args.keys():
        indexToBePopped = []
        if key == 'age':
            argAgeRange = range(int(args['age'])-1, int(args['age'])+2)
        for index in range(len(remainingList)):
            if key == 'age':
                if int(remainingList[index][key]) in argAgeRange:
                    returnList.append(remainingList[index]) 
                    indexToBePopped.append(index)
                    continue
                
            if key in ['name', 'occupation']:
                if args[key].lower() in remainingList[index][key].lower():
                    returnList.append(remainingList[index]) 
                    indexToBePopped.append(index)
                    continue
            if key == 'id':
                if remainingList[index][key] == args[key]:
                    returnList.append(remainingList[index]) 
                    indexToBePopped.append(index)
                    break
        
        # Update the remaining list
        remainingList = [remainingList[index] for index in range(len(remainingList)) if index not in indexToBePopped]     

    return returnList
