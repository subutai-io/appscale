from agents.base_agent import BaseAgent, AgentConfigurationException, AgentRuntimeException
from utils import utils

__author__ = 'akarasulu'
__email__ = 'akarasulu@optimal-dynamics.com'

class SubutaiSocialAgent(BaseAgent):
  """
  Subutai Social infrastructure agent class which can be used to spawn and 
  terminate containers in a Subutai Social environment.
  """

  def configure_instance_security(self, parameters):
    """

    Args:
      parameters  A dictionary of parameters
    """

  def assert_required_parameters(self, parameters, operation):
    """
    Assert that all the parameters required for the SS agent are in place.
    (Also see documentation for the BaseAgent class)

    Args:
      parameters  A dictionary of parameters
      operation   Operations to be invoked using the above parameters
    """

  def run_instances(self, count, parameters, security_configured):
    """

    Args:
      count               No. of VMs to spawned
      parameters          A dictionary of parameters.
      security_configured Uses this boolean value as an heuristic to
                          detect brand new AppScale deployments.

    Returns:
      A tuple of the form (instances, public_ips, private_ips)
    """

  def terminate_instances(self, parameters):
    """

    Args:
      parameters  A dictionary of parameters
    """


  def attach_disk(self, parameters, disk_name, instance_id):
    """

    Args:
      parameters: A dict with keys for each parameter needed.
      disk_name: A str naming the mount to attach to this machine.
      instance_id: A str naming the id of the instance that the disk should be
        attached to. In practice, callers add disks to their own instances.
    Returns:
      The location on the local filesystem where the disk has been attached.
    """

  def handle_failure(self, msg):
    """
    Log the specified error message and raise an AgentRuntimeException

    Args:
      msg An error message to be logged and included in the raised exception

    Raises:
      AgentRuntimeException Contains the input error message
    """
    utils.log(msg)
    raise AgentRuntimeException(msg)
