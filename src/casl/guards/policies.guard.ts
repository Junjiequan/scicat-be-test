import { CanActivate, ExecutionContext, Injectable } from "@nestjs/common";
import { Reflector } from "@nestjs/core";
import { AppAbility, CaslAbilityFactory } from "../casl-ability.factory";
import { CHECK_POLICIES_KEY } from "../decorators/check-policies.decorator";
import { PolicyHandler } from "../interfaces/policy-handler.interface";
import { request } from "https";

@Injectable()
export class PoliciesGuard implements CanActivate {
  constructor(
    private reflector: Reflector,
    private caslAbilityFactory: CaslAbilityFactory,
  ) {}

  async canActivate(context: ExecutionContext): Promise<boolean> {

    const policyHandlers =
    this.reflector.get<PolicyHandler[]>(
      CHECK_POLICIES_KEY,
      context.getHandler(),
    ) || [];

    const req = context.switchToHttp().getRequest();
    const user = req.user;
    const endpoint = req.route.path.split("/")[3]
    
    const ability = this.caslAbilityFactory.accessEndpointForUser(user, endpoint);
    return policyHandlers.every((handler) =>
      this.execPolicyHandler(handler, ability),
    );
  }


  private execPolicyHandler(handler: PolicyHandler, ability: AppAbility) {
    if (typeof handler === "function") {
      const res = handler(ability);
      //console.log("PoliciesGuard:execPolicyHandler ", res);
      return res;
    }
    return handler.handle(ability);
  }
}





    // Assuming that there is only one policy handler, extract the subject
    //const policyHandler = policyHandlers[0];
    //const subject = this.extractSubjectFromPolicyHandler(policyHandler);

  