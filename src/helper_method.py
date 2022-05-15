

class QueryHelper(object):
  """
  Base class for forming query
  """
  def find_user_name(self, user_name):
    """
    Format for tenant name in mongo
    Args:
      user_name (string): user name
    Returns:
      dictionary of requested format
    """
    return {
      'user_name': user_name
    }

  def get_update_query(self, update_data):
    """
    Format for update in mongo
    Args:
      update_data (dict): update_data
    Returns:
      dictionary of requested format
    """
    return {
      "$set": update_data
    }